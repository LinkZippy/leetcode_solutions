-- How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name.

select distinct m.firstname || ' ' || m.surname as member, f.name as facility
from cd.bookings b
join cd.members m on b.memid = m.memid
join cd.facilities f on f.facid = b.facid
where f.name like '%Tennis Court%'
order by member
;
