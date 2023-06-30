# Write your MySQL query statement below
(select U.name as results from Users U, MovieRating M where U.user_id=M.user_id group by M.user_id order by count(*) desc, U.name limit 1)
union all
(select Mo.title as results from Movies Mo, MovieRating MR where Mo.movie_id=MR.movie_id and MR.created_at like "2020-02-%" group by MR.movie_id order by avg(MR.rating) desc, Mo.title limit 1); 