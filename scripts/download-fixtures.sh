#!/usr/bin/env bash

# This script downloads the test data for the project.
# Note: it should run in the project root directory.

## Basic functions
function get-checkin {
  # Get a Rockd checkin by ID
  checkin_id=$1
  outfile=test-data/rockd/checkin-$1.json
  url="https://rockd.org/api/v2/protected/checkins?checkin_id=$checkin_id"
  if [ -f $outfile ]; then
    echo "File $outfile already exists, skipping download."
    return
  fi
  echo "Downloading $url -> $outfile"
  mkdir -p $(dirname $outfile)
  curl -s "$url" | jq '.success.data[0]' > $outfile
}

function get-spot {
  # StraboSpot API documentation
  # https://strabospot.org/api
  spot_id=$1
  outfile=test-data/strabospot/spot-$1.json

  url="https://strabospot.org/db/feature/$spot_id"

  if [ -f $outfile ]; then
    echo "File $outfile already exists, skipping download."
    return
  fi

  # Download the spot data
  echo "Downloading $url -> $outfile"
  mkdir -p $(dirname $outfile)
  curl -u "daven.quinn@wisc.edu:strabospot" -s "$url" | jq '.' > $outfile
}

# Check if we have jq installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found, please install it to run this script."
    exit
fi



# Get a testing spot (complete spot with all fields)
url="https://gist.githubusercontent.com/jasonash/d7a8be8d2e2a11a926f195b8f25106b6/raw/97c5ebd04c1386bf832723e0a50d8c44f1b8b48c/spot.json"
outfile=test-data/strabospot/complete-spot.json
if [ ! -f $outfile ]; then
  echo "Downloading $url -> $outfile"
  mkdir -p test-data/strabospot
  curl -s "$url" \
    | jq '.' \
    > test-data/strabospot/complete-spot.json
fi

# Get checkins and spots
get-checkin 26692

