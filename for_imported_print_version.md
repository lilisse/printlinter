# sys.stdout/stderr/stdin

## import just sys

```python
import sys

sys.stdout.write("a")
```

We have

```python
Expr(
    value=Call(
        func=Attribute(
            value=Attribute(
                value=Name(id="sys", ctx=Load()), attr="stdout", ctx=Load()
            ),
            attr="write",
            ctx=Load(),
        ),
        args=[Constant(value="a")],
        keywords=[],
    )
)
```

We need to test if we have it's 3 conditions:

- node.value.func.value.value.id. = sys
- node.value.func.value.attr = stdout
- node.value.func.aatr = write

It's exactly same for `stderr` and `stdin`.

## import <stdout/stderr/stdin>

```python
from sys import stdout

stdout.write("a")
```

We have

```python
Expr(
    value=Call(
        func=Attribute(value=Name(id="stdout", ctx=Load()), attr="write", ctx=Load()),
        args=[Constant(value="a")],
        keywords=[],
    )
)
```

We need to test if we have it's 2 conditions:

- node.value.func.value.id = stdout
- node.value.func.attr = write

It's exactly same for `stderr` and `stdin`.

## HELP

To print ast repr use

```python
print(ast.dump(tree, indent=4))
```

in the file: `py_printlinter/parser.py`
