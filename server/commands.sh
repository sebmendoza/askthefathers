#!/bin/bash

function start_chroma(){
    chroma run --path ./chroma
}
function act() {
    source venv/bin/activate
}

function deact(){
    deactivate
}