# Pydocxrunner

Is *Word* or *Libre Office Writer* you favorite IDE? Do you recognize *docx* as a superior file format? And are you tired of the high effort required to execute the code stored in `.docx`files? Then don't worry, `pydocxrunner`is the tool of your dreams. `pydocxrunner` provides a simple command to make a `.docx` file executable.

## Features

- Make `.docx`file executable via the `python` command. Once the file is made executable, `pydocxrunner` is no longer required.
- The `.docx` file can then be executed on any device with `python` installed.
- What else do you need?



## Example

Assuming you have a file called `printquad.docx` with the following content:

```python
for i in range(10):
    print(i)
```



Then you can make it executable using `pydocxrunner`:

```sh
$ pydocxrunner printquad.docx
```

And execute it (on any device having `python3` installed):

```sh
$ python3 printquad.docx
0
1
4
9
16
25
36
49
64
81
```



## How it works

Unknown to most, `.docx` files are `.zip` files with a fancy name. Also unknown to most, `python` can execute `.zip` files. `pydocxrunner` writes a simple `__main__.py` file as well as [python-docx2txt](https://github.com/ankushshah89/python-docx2txt) into the `.docx` file. The `__main__.py` script will be executed by the python interpreter and read the contents of the `.docx` file. This content is then passed to an `exec()` call.

## Caveats

- This is not tested beyond a few simple statements
- I do not recommend using this  tool for production
- An internet connection is required when running `pydocxrunner` as `python-docx2txt` needs to be downloaded. No connection is required to actually execute the `.docx` file.



## TODO

- Make this work with other types of documents
- Make this work with other languages
- Find a better solution for installing `python-docx2txt`