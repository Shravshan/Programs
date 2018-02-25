begin;

DROP TABLE IF EXISTS public.temp;
CREATE TABLE public.temp AS
SELECT
a.CID 
,b.*
FROM public.consumers AS a, keyword_consumer AS b
WHERE (strpos(a.contents,b.keyword)>0)
;


DROP TABLE IF EXISTS public.main_c ;
CREATE TABLE public.main_c AS
SELECT 
a.*
,b.keyword
,b.category
,b.sub_category

FROM public.consumers a 
LEFT JOIN 
(SELECT * FROM public.temp
)b
ON a.CID = b.CID
;

DROP TABLE IF EXISTS public.temp_expert;
CREATE TABLE public.temp_expert AS
SELECT
a.CID 
,b.*
FROM public.expert AS a, keyword_expert AS b
WHERE (strpos(a.contents,b.keyword)>0)
;

DROP TABLE IF EXISTS public.main_e ;
CREATE TABLE public.main_e AS
SELECT 
a.*
,b.keyword
,b.category
,b.sub_category

FROM public.expert a 
LEFT JOIN 
(SELECT * FROM public.temp_expert
)b
ON a.CID = b.CID
;

commit;