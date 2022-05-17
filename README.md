This is a test repository for checking the output of QML repo demonstrations.

Produces a markdown file with the difference between the two versions of the
rendered demonstrations from the QML repository.

The file is structured as follows:

* Name of the tutorial (e.g., `tutorial_ensemble_multi_qpu.html`)
* `Master`:
    * Contains a link pointing to the live version of the demo
    * Outputs the lines in the printed results where a difference was detected
* `Dev`:
    * Contains a link pointing to the version of the demo built using the `dev` branch
    * Outputs the lines in the printed results where a difference was detected

Comparing the affected lines in the `master` and `dev` cases should help
determine if there was a non-negligible change in the output of the specific
demonstration.

Non-negligible changes could include:

* Significant changes in the printed results
* New warnings (maybe errors) being emitted
