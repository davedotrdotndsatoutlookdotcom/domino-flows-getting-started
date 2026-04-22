from flytekit import workflow
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask

@workflow
def simple_math_workflow(a: int, b: int) -> float:

    add_task = DominoJobTask(
        name="Add numbers",
        domino_job_config=DominoJobConfig(command="python add.py"),
        inputs={"first_value": int, "second_value": int},
        outputs={"sum": int},
        use_latest=True
    )

    sum = add_task(first_value=a, second_value=b)

    sqrt_task = DominoJobTask(
        name="Square root",
        domino_job_config=DominoJobConfig(command="python sqrt.py"),
        inputs={"value": int},
        outputs={"sqrt": float},
        use_latest=True
    )

    sqrt = sqrt_task(value=sum)

    return sqrt
