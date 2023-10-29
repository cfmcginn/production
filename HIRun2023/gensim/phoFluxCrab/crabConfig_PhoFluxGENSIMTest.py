from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "PhoFluxGENSIMTest_20231029"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "stepGENSIM.py"
config.JobType.pyCfgParams=["maxEventsOutput=350"]
config.JobType.maxMemoryMB = 3000    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

config.section_("Data")
#config.Data.inputDataset = "/PPRefHardProbes0/Run2023F-PromptReco-v1/MINIAOD"
#config.Data.inputDBS = "global"
config.Data.outputPrimaryDataset = "PhoFluxPYTHIA8"
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 100
config.Data.totalUnits = 100
config.Data.outputDatasetTag = "PhoFluxGENSIMTest_20231029"
config.Data.outLFNDirBase = "/store/group/phys_heavyions/cmcginn/"
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
