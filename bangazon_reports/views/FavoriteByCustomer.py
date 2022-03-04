from django.shortcuts import render
from django.db import connection
from django.views import View
from bangazon_reports.views.helpers import dict_fetch_all



class FavoriteStoreList(View):
    def get(self, request):
        """get favorites by customer"""
        with connection.cursor() as db_cursor:
            
            db_cursor.execute("""
                select  f.id, 
                        c.id as customer_id,
                        c.first_name as customer_name,
                        s.id as store_id,
                        s.name as store_name
                        from bangazon_api_favorite f
                        join bangazon_api_store s on f.store_id = s.id
                        join auth_user c on f.customer_id = c.id
            """)
            
            dataset = dict_fetch_all(db_cursor)
            
            favorites_by_user = []
            
            for row in dataset:
                store = {
                    'store': row['store_name']
                }
                user_dict = next(
                    (
                        customer for customer in favorites_by_user
                        if customer['customer_id'] == row['customer_id']
                    ),
                    None
                )
                if user_dict:                    
                    user_dict['store'].append(store)
                else:
                    favorites_by_user.append({
                        "customer_id": row['customer_id'],
                        "customer_name": row['customer_name'],
                        "stores": [store]
                    })
                    
            template = 'users/favoriteByCustomer.html'
            context = {
                "favorite_store_list": favorites_by_user
            }
            
            return render(request, template, context)