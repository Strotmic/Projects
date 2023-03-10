select customerid, name,address, zipcode,balance from tblcustomers where balance >=150 and balance <=300 order by balance desc;
select lastname, firstname, birthdate from tblemployees where month(BirthDate)!=8 and month(BirthDate)!=7;
select lastname, firstname, birthdate from tblemployees; -- where birthdate;
use artemis;
select employeeid, lastname, firstname, birthdate from tblemployees where date(birthdate) between '1960-01-01 00:00:00.000000' and '1966-01-27 23:59:59.999999';
select name, city from tblcustomers where city in ('Leuven','Herent','Kessel-Lo','Heverlee');
select name, city from tblcustomers where city not in ('Leuven','Herent','Kessel-Lo','Heverlee');
select concat(nederlandsenaam ,' (', productname , ' )') from tblproducts where categorynumber in (1,2,3,4,8);
select productname from tblproducts where nederlandsenaam like '%thee%';
select productname, priceperunit from tblproducts where (nederlandsenaam like '%kaas%' or nederlandsenaam like '%vlees%') and (priceperunit <32);
select concat(name, ' ' , city) as 'Customer name' from tblcustomers where name like 'Vander%t';
select concat(name, ' ' , city) as 'Customer name' from tblcustomers where address like '%dorp%';
select company from tblsuppliers where company like '%an%' or company like '%foot%';
select productname from tblproducts where productname like 'Chef%mix';
select productname from tblproducts where binary productname like '%c%' or productname like '%y%' or binary productname like '%B%';
select customerid from tblcustomers where balance >999;
select taxpercentage from tbltaxrate where taxpercentage REGEXP '[0-9].[0-9][0-9]';
select taxpercentage from tbltaxrate where taxpercentage REGEXP '[0-9][0-9][0-9]';
select name, type from tblcustomers where type in('T','W') order by type desc, name asc;
select name, balance, city from tblcustomers where balance >0 order by balance desc;
select concat(lastname , ' ' , firstname) as name, birthdate from tblemployees order by birthdate asc;
select lastname, firstname, city, employed from tblemployees where year(employed)=1993;
select name, city from tblcustomers where city in ('Leuven') order by name asc;
select lastname, firstname, gender from tblemployees where gender = 2 and city = 'Leuven';
select firstname, lastname from tblemployees where gender=1 and city not in ('Leuven', 'Kessel-Lo','Herent');
select name, balance, customerid from tblcustomers where balance >175 order by name asc;
select name from tblcustomers where name like 'Van%';
select upper(city), upper(lastname) from tblemployees where jobtitle='Vertegenwoordiger' and city not in ('Genk','Herent','Leuven','Peer');
select productname, stock, onorder, shop, (stock - onorder) as 'Pressing shortages' from tblproducts where stock-onorder<shop order by stock-onorder asc;
select concat(company, ' ' , country) from tblsuppliers where country not in ('Spanje', 'Verenigd Koninkrijk') order by company asc limit 5;
select distinct country from tblsuppliers;
select count(distinct registrationnumber) as 'number of customers', sum(balance) as balance from tblcustomers;
select count(orderdate) from tblorders where orderdate='2006-08-06';
select avg(priceperunit * 1.10) from tblproducts;
select lastname, firstname from tblemployees where jobtitle='Vertegenwoordiger' and year(employed)<1993;
select max(year(birthdate)) - min(year(birthdate)) as 'maximum difference on date of birth' from tblemployees where city='Leuven';
select count(orderdate) from tblorders where year(orderdate)=2005;
select concat(round(avg(wage),2), ' ',' $') from tblemployees;
select count(employeeid) from tblemployees where gender=1;
select concat(round(max(priceperunit) - min(priceperunit),2),' ' ,' $' ) from tblproducts;
select count(customerid) from tblcustomers where city='Brussel';
select orderdate from tblorders where date(deliverydate) is null;
select avg(datediff(expirationdate,orderdate)) from tblorders where date(deliverydate) is not null;
select orderid, customernumber,dayname(deliverydate) from tblorders where weekday(deliverydate) not in ('0','4') order by weekday(deliverydate) asc;
select count(firstname), round(avg(datediff(now(),birthdate)/365)) from tblemployees where gender=2;
select count(firstname), round(avg(datediff(now(),birthdate)/365),1) from tblemployees where gender=2;

