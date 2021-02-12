from define.algo import Step


def test_step_to_html(step):
    step.text = "hello"
    assert step.html == "<li>hello</li>"


def test_root_step_to_html(step):
    step.substeps = [Step("first"), Step("second")]
    assert step.html == "<ol><li>first</li><li>second</li></ol>"


def test_step_with_substeps(step):
    step.text = "top"
    step.substeps = [Step("first"), Step("second")]
    assert step.html == "<li>top</li><ol><li>first</li><li>second</li></ol>"
