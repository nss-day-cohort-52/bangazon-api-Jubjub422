select  f.id, 
                        c.id as customer_id,
                        c.first_name as customer_name,
                        s.id as store_id,
                        s.name as store_name
                        from bangazon_api_favorite f
                        join bangazon_api_store s on f.store_id = s.id
                        join auth_user c on f.customer_id = c.id

 select  o.id as orderproduct_id,
                        c.first_name as first_name,
                        c.last_name as last_name,
                        op.id as order_id,
                        op.created_on,
                        p.price as price
                        from bangazon_api_orderproduct o
                        join bangazon_api_order op on op.id = o.order_id
                        join auth_user c on c.id = op.user_id
                        join bangazon_api_product p on p.id = o.product_id
                        where completed_on is NULL
                        order by op.created_on