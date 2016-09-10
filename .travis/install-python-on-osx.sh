#!/bin/bash

set -e
set -x

if [[ $TRAVIS_OS_NAME == 'osx' ]]
then
  # install pyenv
  git clone https://github.com/yyuu/pyenv.git ~/.pyenv
  PYENV_ROOT="$HOME/.pyenv"
  PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init -)"

  case "${TOXENV}" in
      py27)
          curl -O https://bootstrap.pypa.io/get-pip.py
          python get-pip.py --user
          ;;
      py33)
          pyenv install 3.3.6
          pyenv global 3.3.6
          ;;
      py34)
          pyenv install 3.4.5
          pyenv global 3.4.5
          ;;
      py35)
          pyenv install 3.5.2
          pyenv global 3.5.2
          ;;
  esac

	pyenv rehash
  python --version
  python -m pip install --user virtualenv
fi

python -m virtualenv ~/.venv
