from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime

with DAG(
    dag_id='ssh_example',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    run_remote_command = SSHOperator(
        task_id='run_command_on_remote',
        ssh_conn_id='sparkssh', # 위에서 설정한 Conn Id
        command='/home/dbsys/sparkclient/collect.sh', # 실행할 원격 명령어
        # 이외에도 bash_command, script, get_conn 등 다양한 옵션이 있습니다.
    )
