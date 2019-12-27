SELECT 
  s.store_id, 
  a.address, 
  a.address2, 
  a.district, 
  c.city, 
  co.country, 
  a.postal_code, 
  st.first_name as manager_first_name, 
  st.last_name as manager_last_name
FROM 
  `databig-260523.staging.stores` s
JOIN 
  `databig-260523.staging.staffs` st on (s.manager_staff_id = st.staff_id)
JOIN 
  `databig-260523.staging.address` a on (s.address_id = a.address_id)
JOIN 
  `databig-260523.staging.cities` c on (a.city_id = c.city_id)
JOIN 
  `databig-260523.staging.countries` co on (c.country_id = co.country_id);


-- SELECT  s.store_id, a.address, a.address2, a.district, c.city, co.country, a.postal_code, st.first_name as manager_first_name, st.last_name as manager_last_name
-- FROM `databig-260523.staging.stores` s
-- JOIN `databig-260523.staging.staffs` st on (s.manager_staff_id = st.staff_id)
-- JOIN `databig-260523.staging.address` a on (s.address_id = a.address_id)
-- JOIN `databig-260523.staging.cities` c on (a.city_id = c.city_id)
-- JOIN `databig-260523.staging.countries` co on (c.country_id = co.country_id);