create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;


-- Pizza places that open before 1pm in alphabetical order
create table opening as
  select name from pizzas where open < 13 order by name desc;

-- Two meals at the same place
create table double as
  select b.meal, c.meal, a.name
  from pizzas as a, meals as b, meals as c
  where c.time - b.time > 6 and b.time >= a.open and c.time <= a.close;

