-- Table: public.p_roads

-- DROP TABLE IF EXISTS public.p_roads;

CREATE TABLE IF NOT EXISTS public.p_roads
(
    gid integer NOT NULL DEFAULT nextval('p_roads_gid_seq'::regclass),
    linearid character varying(22) COLLATE pg_catalog."default",
    fullname character varying(100) COLLATE pg_catalog."default",
    rttyp character varying(1) COLLATE pg_catalog."default",
    mtfcc character varying(5) COLLATE pg_catalog."default",
    geom geometry(MultiLineString,4326),
    CONSTRAINT p_roads_pkey PRIMARY KEY (gid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.p_roads
    OWNER to "Mihriban";
-- Index: p_roads_geom_idx

-- DROP INDEX IF EXISTS public.p_roads_geom_idx;

CREATE INDEX IF NOT EXISTS p_roads_geom_idx
    ON public.p_roads USING gist
    (geom)
    TABLESPACE pg_default;
