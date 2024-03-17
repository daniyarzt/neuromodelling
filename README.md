
## Getting Started with the dataset 

Follow `install-guide.pdf` on BlackBoard. I recommend going through `example_allensdk.ipynb` notebook to understand what is feasible. 

## Description of the dataset 

### Extracellular Electrophysiology Data (From the official [guide](https://allensdk.readthedocs.io/en/latest/_static/examples/nb/ecephys_session.html))
At the Allen Institute for Brain Science we carry out in vivo extracellular electrophysiology (ecephys) experiments in awake animals using high-density Neuropixels probes. The data from these experiments are organized into sessions, where each session is a distinct continuous recording period. During a session we collect:

- spike times and characteristics (such as mean waveforms) from up to 6 neuropixels probes
- local field potentials
behavioral data, such as running speed and eye position
- visual stimuli which were presented during the session
- cell-type specific optogenetic stimuli that were applied during the session

The AllenSDK contains code for accessing across-session (project-level) metadata as well as code for accessing detailed within-session data. The standard workflow is to use project-level tools, such as `EcephysProjectCache` to identify and access sessions of interest, then delve into those sessions' data using `EcephysSession`.

## Current Ideas

### Detecting 'Confusion'
" Use the first 3 seconds of neural readings to predict IF the mouse WILL manage to click the button at correct time. Usual direction of neural readings is like 10sec I think. This is basically akin to detecting "confusion" patterns in the brain early on: can initial confusion accurately predict the final outcome? " @ Andrey

### Post-stimuli classification
Professor provided example where they classify the label of the image stimuli, using spike data. During the stimuli, for each neuron the aggregate how many times it fired and use this vectors to classify the type of the image presented. 

We can extend this idea further, and take the spike data after the stimuli was shown and see if it is useful in classification. This way we see if signal remain 'in memory' and for how long. We could also see if there is a shift in brain region that contain the useful signal. 