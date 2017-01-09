from multi_server_workers import celeryapp

task = celeryapp.send_task("multi_server_workers.tasks.add",
                         kwargs={"x":12, "y":40})

