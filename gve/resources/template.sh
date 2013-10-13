#!/bin/sh

PROJECT={{currentdir}}

echo 'Activating environment in ' $PROJECT

GOENV=$PROJECT/env
DEPS=$GOENV/deps

echo 'Configuring $GOPATH'
GOPATH=$DEPS:$PROJECT:$DEPS
echo 'Configuring $PATH'
PATH=$PROJECT/bin:$DEPS/bin:$PATH

export GOPATH
export PATH

echo 'Environment has been activated'
