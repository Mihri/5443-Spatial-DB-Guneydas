-- Table: public.rails

-- DROP TABLE IF EXISTS public.rails;

CREATE TABLE IF NOT EXISTS public.rails
(
    gid integer NOT NULL DEFAULT nextval('rails_gid_seq'::regclass),
    linearid character varying(22) COLLATE pg_catalog."default",
    fullname character varying(100) COLLATE pg_catalog."default",
    mtfcc character varying(5) COLLATE pg_catalog."default",
    geom geometry(MultiLineString,4326),
    CONSTRAINT rails_pkey PRIMARY KEY (gid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.rails
    OWNER to "Mihriban";
-- Index: rails_geom_idx

-- DROP INDEX IF EXISTS public.rails_geom_idx;

CREATE INDEX IF NOT EXISTS rails_geom_idx
    ON public.rails USING gist
    (geom)
    TABLESPACE pg_default;
