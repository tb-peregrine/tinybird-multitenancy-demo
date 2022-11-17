# Shared Workspace multi-tenancy example in Tinybird

Use these files to recreate a simple multi-tenancy example in Tinybird using a shared Workspace and per-tenant Data Sources created from Materialized Views.

## Steps

Install the Tinybird CLI:

```bash
python3 -m venv .e
. .e/bin/activate

pip install tinybird-cli
```

Authenticate:

```bash
tb auth --interactive
```
Choose your region: **1** for *US-East* and **2** for *EU*.

Go to your Workspace at ui.tinybird.co (or ui.us-east.tinybird.co) and copy your User Admin Auth Token from the Workspace and paste it to authenticate.

## Project Description

```bash
├── datasources
│   └── landing_datasource.datasource
│   └── tenant_1_ds.datasource
│   └── tenant_2_ds.datasource
│   └── ...
│   └── tenant_n_ds.datasource
├── pipes
│   └── tenant_1_pipe.pipe
│   └── tenant_2_pipe.pipe
│   └── ..
│   └── tenant_n_pipe.pipe
├── endpoints
│   └── tenant_1_usage_current_month.pipe
│   └── tenant_2_usage_current_month.pipe
│   └── ..
│   └── tenant_n_usage_current_month.pipe
```

In the `/datasources` folder, you'll find the landing Data Source where all tenant data is initially ingested. Each `tenant_n_pipe.pipe` selects only rows for `tenant_id = n`, then materializes them into `tenant_n_ds`. Some example endpoints (e.g. `tenant_n_usage_current_month.pipe`) demonstrate the functionality.

## Push the Data Project to Tinybird
After you clone the repo, push the Data Project to Tinybird:

```bash
tb push --no-check
```

## Stream activity events data with the Events API

Use `genereate_events.py` to begin streaming randomized events into the landing Data Source:

```bash
python3 generate_events.py
```

## Automate new tenant assets

If you want to automate the creation of a Pipe, Materielized Data Source, and Endpoint for a new, numbered tenant, use `automate.sh`, passing the tenant ID as an argument:

```bash
. ./automate.sh $TENANT_ID
```

> **NOTE:** You'll need to set your User Admin token as an environment variable to run that script.
