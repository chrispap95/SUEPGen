import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.0),
    maxEventsToPrint = cms.untracked.int32(1),
    UserCustomization = cms.VPSet(
        cms.PSet(
            pluginName = cms.string("SuepDecay"),
            temperature = cms.double(0.5),
            idMediator = cms.int32(25),
            idDark = cms.int32(999999),
        )
    ),
    crossSection = cms.untracked.double(1.0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'Check:event = off',
            # parameters for mediator (Higgs)
            'Higgs:useBSM = on',
            'HiggsBSM:gg2H1 = on',
            'HiggsH1:coup2d = 1',
            'HiggsH1:coup2u = 0',
            'HiggsH1:coup2Z = 0',
            'HiggsH1:coup2W = 0',
            'HiggsH1:coup2l = 0',
            '25:m0 = 125.0',
            # add a dark meson and dark photon
            '999999:all = GeneralResonance void 0 0 0 2.0 0.001 0.0 0.0 0.0',
            '999998:all = GeneralResonance void 1 0 0 0.7 0.001 0.0 0.0 0.0',
            # define dark meson decay
            '999999:addChannel = 1 1.0 101 999998 999998', # 100% br to dark photons
            '999998:addChannel = 1 0.15 101 11 -11',
            '999998:addChannel = 1 0.15 101 13 -13',
            '999998:addChannel = 1 0.70 101 211 -211',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters',
        )
    )
)
