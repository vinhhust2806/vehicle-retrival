# Natural Language-Based Vehicle Retrieval

This dataset is curated for the Natural Language (NL) Based Vehicle Retrieval
Challenge Track of the 2022 AI City Workshop. Please refer to our GitHub repo
for more information: https://github.com/fredfung007/cityflow-nl.git

## Contents in this repository

`extract_vdo_frms.py` is a Python script that is used to extract frames from
videos provided in the Multi-Target Multi-Camera Tracking (MTMC) Challenge Track
of the 2022 AI City Challenge. Please use this script to extract frames, so that
the path configurations in JSON files are consistent.

`train_tracks.json` is a dictionary of all 2,155 vehicle tracks in the
training split. Each vehicle track is annotated with three natural language (NL)
descriptions of the target and is assigned a universally unique identifier
(UUID). The file is structured as

```json
{
  "track-uuid-1": {
    "frames": ["file-1.jpg", ..., "file-n.jpg"],
    "boxes": [[742, 313, 171, 129], ..., [709, 304, 168, 125]],
    "nl": [
      "A gray pick-up truck goes ...",
      "A dark pick-up runs ...",
      "Pick-up truck that goes ..."
    ],
    "nl_other_views": [
      "A gray pick-up turns right ...",
      "A pick-up stops ...",
      "A Ford truck goes ...",
      ...
    ]
  },
  "track-uuid-2": ...
}
```

The files under the `frames` attribute are paths in the CityFlow Benchmark [2]
used in the MTMC challenge. The `nl` attribute contains the three natural
language descriptions annotated for this vehicle track. The `nl_other_views`
attribute is a list of all other natural language descriptions we collected for
the same vehicle target, but for another view point or another time.

`test_tracks.json` contains 184 tracks of candidate target vehicles. The
structure of this file is identical to the training split, except that the
natural language descriptions are removed.

`test_queries.json` contains 184 queries. Each consists of three natural
language descriptions of the vehicle target annotated by different annotators
under the `nl` attributes. Same as the training split, the `nl_other_views` is a
list of all other natural language descriptions we collected for the same
vehicle target, but for another view point or another time. Teams may choose to
use these additional descriptions during inference if needed. Each query is
assigned a UUID that is later used in results submission. The structure of this
file is as follows:

```json
{
  "query-uuid-1": {
    "nl": [
      "Blue truck runs down the street.",
      "A blue pickup truck drives through an intersection.",
      "A blue pickup truck going straight down the street passing an intersection."
    ],
    "nl_other_views": [
      "A dark blue pickup drives through an intersection.",
      "A blue pickup moves through the intersection.",
      ...
    ]
  },
  "query-uuid-2": ...
}
```

## Problem Definition

Teams should retrieve and rank the provided vehicle tracks for each of the
queries. A baseline retrieval model is provided as a demo for a start point for
participating teams.

## Usage of Pre-trained Models and Additional Data

Teams **cannot** use models that are pre-trained on the CityFlow Benchmark,
*e.g.* ResNet used for the Re-ID or MTMC tracks in previous AI City Challenges.
Teams may use additional publicly available training datasets that were not
collected specifically for language-based, traffic-related vision tasks. If in
doubt, please contact the organizers.

## Submission Format

For each query, teams should submit a list of the testing tracks ranked by their
retrieval model. One JSON file should be submitted containing a dictionary in
the following format:

```json
{
  "query-uuid-1": ["track-uuid-i", ..., "track-uuid-j"],
  "query-uuid-2": ["track-uuid-m", ..., "track-uuid-n"],
  ...
}
```

## Evaluation Metrics

The Vehicle Retrieval by NL Descriptions task is evaluated using standard
metrics for retrieval tasks. We use the Mean Reciprocal Rank (MRR) [3] as the
main evaluation metric. Recall @ 5, Recall @ 10, and Recall @ 25 are also
evaluated for all submissions.

## Citations

Please cite this work:

[1] Feng, Qi, et al. "CityFlow-NL: Tracking and Retrieval of Vehicles at City
Scale by Natural Language Descriptions." arXiv preprint. arXiv:2101.04741.

## References

[2] Tang, Zheng, et al. "CityFlow: A city-scale benchmark for multi-target
multi-camera vehicle tracking and re-identification." CVPR. 2019.

[3] Voorhees, Ellen M. "The TREC-8 question answering track report." Trec. Vol. 99. 1999.
