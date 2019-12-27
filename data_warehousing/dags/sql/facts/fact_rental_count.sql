create table 'databig-260523.warehouse.fact_customer_count' (
  rental_count_key int64 not null,
  date_key int64 not null,
  store_key int64 not null,
  sales_key int64 not null,
  customer_count float64 not null
);