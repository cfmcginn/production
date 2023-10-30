from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "forest_miniAOD_run3_ppref_Data_PPRefHardProbes1"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "forest_miniAOD_run3_ppref_Data.py"
config.JobType.maxMemoryMB = 3000    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

config.section_("Data")
config.Data.inputDataset = "/PPRefHardProbes1/Run2023F-PromptReco-v1/MINIAOD"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "forest_miniAOD_run3_ppref_Data_PPRefHardProbes1"
config.Data.outLFNDirBase = "/store/group/phys_heavyions/cmcginn/"
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
