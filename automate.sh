python -m venv .e
. .e/bin/activate
pip install tinybird-cli
tb init
tb auth --token $TOKEN
tb pipe generate tenant_$1_pipe "select * from landing_datasource where tenant_id = $1"
mv endpoints/tenant_$1_pipe.pipe pipes/tenant_$1_pipe.pipe
echo '1\n' | tb materialize pipes/tenant_$1_pipe.pipe tenant_$1_ds
tb pipe generate tenant_$1_usage_current_month "select count() from tenant_$1_ds where toStartOfMonth(timestamp) = toStartOfMonth(now())"
tb push endpoints/tenant_$1_usage_current_month.pipe --push-deps
deactivate
rm -r .e
