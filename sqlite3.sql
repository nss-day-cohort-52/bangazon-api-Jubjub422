select  f.id, 
                        c.id as customer_id,
                        c.first_name as customer_name,
                        s.id as store_id,
                        s.name as store_name
                        from bangazon_api_favorite f
                        join bangazon_api_store s on f.store_id = s.id
                        join auth_user c on f.customer_id = c.id