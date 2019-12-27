SELECT
  c.customer_id, 
  c.first_name, 
  c.last_name, 
  c.email, 
  a.address, 
  a.address2, 
  a.district,
  ci.city, 
  co.country, 
  postal_code,
  a.phone,
  c.active, 
  c.create_date
FROM 
  `databig-260523.staging.customers`  c
JOIN 
  `databig-260523.staging.address` a on (c.address_id = a.address_id)
JOIN 
  `databig-260523.staging.cities` ci on (a.city_id = ci.city_id)
JOIN 
  `databig-260523.staging.countries` co on (ci.country_id = co.country_id)
WHERE c.customer_id > 10;


-- SELECT c.customer_id, c.first_name, c.last_name, c.email, a.address, a.address2, a.district, ci.city, co.country, postal_code, a.phone, c.active, c.create_date
-- FROM `databig-260523.staging.customers`  c
-- JOIN `databig-260523.staging.address` a on (c.address_id = a.address_id)
-- JOIN `databig-260523.staging.cities` ci on (a.city_id = ci.city_id)
-- JOIN `databig-260523.staging.countries` co on (ci.country_id = co.country_id)
-- WHERE c.customer_id > 10;