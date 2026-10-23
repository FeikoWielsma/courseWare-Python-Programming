"""Run the dashboard demos and solution offline, and drive both Streamlit apps."""

import sys

from check_support import run_case, workspace
from streamlit.testing.v1 import AppTest


def metrics(app: AppTest) -> list[str]:
    return [metric.value for metric in app.metric]


def main() -> int:
    failed = 0
    with workspace() as (course, environment):
        demos = "demos/10-dashboards"
        solution = "solutions/solution10-dashboards"
        for relative, label, quoted in [
            (f"{demos}/03_store_in_sqlite.py", "first", "8045 new readings"),
            (f"{demos}/03_store_in_sqlite.py", "second", "0 new readings 8045 readings stored"),
            (f"{demos}/05_resample.py", "", "2672 readings, 672 hours"),
            (f"{solution}/store.py", "first", "8045 new readings 2012 hourly statistics"),
            (f"{solution}/store.py", "second", "0 new readings 2012 hourly statistics"),
        ]:
            failed += not run_case(course, environment, relative, label=label, quoted=quoted)

        demo = AppTest.from_file(str(course / demos / "07_dashboard.py")).run(timeout=60)
        demo.selectbox[0].select("sensor.outdoor_temperature").run(timeout=60)
        demo.slider[0].set_value(28).run(timeout=60)
        answer = AppTest.from_file(str(course / solution / "dashboard.py")).run(timeout=60)
        answer.selectbox[0].select("sensor.outdoor_temperature").run(timeout=60)
        for name, app, expected in [
            ("demo07", demo, ["5.6", "4.0", "18.1"]),
            ("solution dashboard", answer, ["4.0", "18.1"]),
        ]:
            charts = app.get("plotly_chart")
            passed = not app.exception and metrics(app) == expected and len(charts) == 1
            print(f"{'PASS' if passed else 'FAIL'} {name} {metrics(app)}")
            failed += not passed
    print(f"dashboard checks: {failed} failed")
    return int(failed > 0)


if __name__ == "__main__":
    sys.exit(main())
