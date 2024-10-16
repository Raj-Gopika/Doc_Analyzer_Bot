#Importing necessary packages
#import pydantic and pymongo for data modelling and MongoDB
from pydantic import BaseModel
import pymongo

#import traceback for error handling
import traceback
#import os and sys for system related operations
import sys
import os

#import fastapi submodules for craeting web applications
from fastapi import (
    FastAPI,
    UploadFile,
    status,
    HTTPException
)
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


#import langchain for building applications powerd by language models
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader

import gc
import urllib.parse

import awswrangler as wr

import boto3

#Setting up the environment and defining variables for aws S3 config

os.environ['OPENAI_API_KEY'] = "sk-2EmLWS4DTNDr3tD9rpXKQ1B6j_Oze0M_Gy8VatebjAT3BlbkFJ2K1PwuJutCsxODwWG6tM5byJrMztSPetUIdFWuuxYA"
S3_KEY=""
S3_SECRET=""
S3_BUCKET=""
S3_REGION=""
S3_PATH=""