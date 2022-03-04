from django.shortcuts import render
from django.db import connection
from django.views import View
from bangazon_reports.views.helpers import dict_fetch_all


class IncompleteOrderList(View):
    def get(self, request):
        """get all incomplete orders"""
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                select  o.id as orderproduct_id,
                        c.first_name as first_name,
                        c.last_name as last_name,
                        op.id as order_id,
                        op.created_on,
                        SUM(p.price) as price
                        from bangazon_api_orderproduct o
                        join bangazon_api_order op on op.id = o.order_id
                        join auth_user c on c.id = op.user_id
                        join bangazon_api_product p on p.id = o.product_id
                        where completed_on is NULL
                        group by o.order_id
                        order by op.created_on
            """)
            dataset = dict_fetch_all(db_cursor)
            
            incomplete_orders = []
            
            for row in dataset:
                order = {
                    'id': row['order_id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'total': row['price']
                }
                incomplete_orders.append(order)
                
        template = 'users/incompleteOrders.html'
        context = {
            'incomplete_list': incomplete_orders
        }
        return render(request, template, context)