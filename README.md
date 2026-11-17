# Testing Tutorial

Tutorial material: small Python examples of unit, integration and performance testing, plus why error handling and logging matter.

| Folder | What it shows |
|---|---|
| `Calculator/` | A calculator class with unit tests, integration tests (`unittest`) and a simple performance check |
| `Divide_Func_Error Handling&logging_BestPractice/` | A divide function before and after proper error handling and logging, with tests for both |

## Run the tests

```bash
cd Calculator
python -m unittest discover -s test_app -t . -p "*test*.py"
```
