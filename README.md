# pytest-vs-unittest
Comparison between pytest and unittes test frameworks

##Comparison Table

| Feature                    | Pytest                             | Unittest                         | Winner   |
|----------------------------|------------------------------------|----------------------------------|----------|
| Installation               | Third Party                        | Built in                         | Unittest |
| Basic Infra                | Can be only a function             | Inheritance                      | Pytest   |
| Basic Assertion            | Builtin assert                     | TestCase instance methods        | Pytest   |
| Flat is better than nested | Function (1 level)                 | Method (2 level)                 | Pytest   |
| Can run each other test    | Can run unittest tests             | Can't pytest test                | Pytest   |
| Test Result on console     |       |                   |    |
| Multi param test           |          |   |    |
| Test setup                 |  |  |    |
| Name Refactoring           |   |  |  |
| Running Failed Tests       |                |                       |    |
| Marks                      |                            |                       |    |
