create table `databig-260523.warehouse.fact_sales` (
  sales_key int64 not null,
  date_key int64 not null,
  customer_key int64 not null,
  film_key int64 not null,
  store_key int64 not null,
  sales_amount float64 not null
)