SELECT 
  f.film_id, 
  f.title, 
  f.description, 
  f.release_year,
  l.name as language, 
  null as original_language,
  f.rental_duration, 
  f.length, 
  f.rating, 
  f.special_features
FROM 
  `databig-260523.staging.films` f
JOIN 
  `databig-260523.staging._languages_` l on (f.language_id = l.language_id)

-- SELECT f.film_id, f.title, f.description, f.release_year, l.name as language, null as original_language, f.rental_duration, f.length, f.rating, f.special_features
-- FROM `databig-260523.staging.films` f
-- JOIN `databig-260523.staging._languages_` l on (f.language_id = l.language_id)