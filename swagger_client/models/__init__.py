# coding: utf-8

# flake8: noqa
"""
    Teleagronom

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.activation import Activation
from swagger_client.models.agrochemical_analysis_serializer_ import AgrochemicalAnalysisSerializer_
from swagger_client.models.agrochemical_calculator import AgrochemicalCalculator
from swagger_client.models.agrochemical_calculator_detail import AgrochemicalCalculatorDetail
from swagger_client.models.agrochemicalcalculator_create_calculator import AgrochemicalcalculatorCreateCalculator
from swagger_client.models.agrochemicalcalculator_set_report import AgrochemicalcalculatorSetReport
from swagger_client.models.all_of_agrochemical_calculator_detail_normative_calculator import AllOfAgrochemicalCalculatorDetailNormativeCalculator
from swagger_client.models.all_of_agrochemical_calculator_detail_rb_calculator import AllOfAgrochemicalCalculatorDetailRbCalculator
from swagger_client.models.all_of_determinant_progress_disease import AllOfDeterminantProgressDisease
from swagger_client.models.all_of_fluid_calculator_detail_consumption_rate_from_catalog import AllOfFluidCalculatorDetailConsumptionRateFromCatalog
from swagger_client.models.all_of_fluid_consumption_rate_through_nozzle_nozzle_color import AllOfFluidConsumptionRateThroughNozzleNozzleColor
from swagger_client.models.all_of_fluid_consumption_rate_through_nozzle_nozzle_pressure import AllOfFluidConsumptionRateThroughNozzleNozzlePressure
from swagger_client.models.all_of_microorganisms_genus_mycobiota_type import AllOfMicroorganismsGenusMycobiotaType
from swagger_client.models.all_of_mycological_calculator_detail_culture import AllOfMycologicalCalculatorDetailCulture
from swagger_client.models.all_of_mycological_calculator_detail_preceding_culture import AllOfMycologicalCalculatorDetailPrecedingCulture
from swagger_client.models.all_of_normative_calculator_detail_acidity_group import AllOfNormativeCalculatorDetailAcidityGroup
from swagger_client.models.all_of_normative_calculator_detail_culture import AllOfNormativeCalculatorDetailCulture
from swagger_client.models.all_of_normative_calculator_detail_fertilizer_k import AllOfNormativeCalculatorDetailFertilizerK
from swagger_client.models.all_of_normative_calculator_detail_fertilizer_n import AllOfNormativeCalculatorDetailFertilizerN
from swagger_client.models.all_of_normative_calculator_detail_fertilizer_p import AllOfNormativeCalculatorDetailFertilizerP
from swagger_client.models.all_of_normative_calculator_detail_mechanical_composition import AllOfNormativeCalculatorDetailMechanicalComposition
from swagger_client.models.all_of_normative_calculator_detail_preceding_culture import AllOfNormativeCalculatorDetailPrecedingCulture
from swagger_client.models.all_of_normative_calculator_detail_region import AllOfNormativeCalculatorDetailRegion
from swagger_client.models.all_of_normative_calculator_region_culture_combination_view_culture import AllOfNormativeCalculatorRegionCultureCombinationViewCulture
from swagger_client.models.all_of_normative_calculator_region_culture_combination_view_region import AllOfNormativeCalculatorRegionCultureCombinationViewRegion
from swagger_client.models.all_of_rb_calculator_culture import AllOfRbCalculatorCulture
from swagger_client.models.all_of_rb_calculator_detail_culture import AllOfRbCalculatorDetailCulture
from swagger_client.models.all_of_rb_calculator_detail_degree_of_soil_moisture import AllOfRbCalculatorDetailDegreeOfSoilMoisture
from swagger_client.models.all_of_rb_calculator_detail_depth_of_arable_layer import AllOfRbCalculatorDetailDepthOfArableLayer
from swagger_client.models.all_of_rb_calculator_detail_fertilizer_action_year import AllOfRbCalculatorDetailFertilizerActionYear
from swagger_client.models.all_of_rb_calculator_detail_fertilizer_k import AllOfRbCalculatorDetailFertilizerK
from swagger_client.models.all_of_rb_calculator_detail_fertilizer_n import AllOfRbCalculatorDetailFertilizerN
from swagger_client.models.all_of_rb_calculator_detail_fertilizer_p import AllOfRbCalculatorDetailFertilizerP
from swagger_client.models.all_of_rb_calculator_detail_mechanical_composition import AllOfRbCalculatorDetailMechanicalComposition
from swagger_client.models.all_of_rb_calculator_detail_region import AllOfRbCalculatorDetailRegion
from swagger_client.models.all_of_rb_calculator_region import AllOfRbCalculatorRegion
from swagger_client.models.all_of_rb_calculator_region_culture_combination_view_culture import AllOfRbCalculatorRegionCultureCombinationViewCulture
from swagger_client.models.all_of_rb_calculator_region_culture_combination_view_region import AllOfRbCalculatorRegionCultureCombinationViewRegion
from swagger_client.models.all_of_rosselkhoz_bank_agrochemical_analysis_request_agrochemical_calculator import AllOfRosselkhozBankAgrochemicalAnalysisRequestAgrochemicalCalculator
from swagger_client.models.all_of_rosselkhoz_bank_complex_analysis_request_agrochemical_calculator import AllOfRosselkhozBankComplexAnalysisRequestAgrochemicalCalculator
from swagger_client.models.answer_question import AnswerQuestion
from swagger_client.models.application_area import ApplicationArea
from swagger_client.models.causative_agent import CausativeAgent
from swagger_client.models.chemical_class import ChemicalClass
from swagger_client.models.coefficient_conversion_of_nutrients import CoefficientConversionOfNutrients
from swagger_client.models.coefficient_depending_on_mechanical_soil_composition import CoefficientDependingOnMechanicalSoilComposition
from swagger_client.models.coefficient_depending_on_quality_predecessor import CoefficientDependingOnQualityPredecessor
from swagger_client.models.coefficient_depending_on_soil_acidity import CoefficientDependingOnSoilAcidity
from swagger_client.models.coefficient_fertilization_per_crop_ton import CoefficientFertilizationPerCropTon
from swagger_client.models.coefficient_removal_of_nutrients import CoefficientRemovalOfNutrients
from swagger_client.models.coefficient_utilization_factor import CoefficientUtilizationFactor
from swagger_client.models.coefficient_utilization_nutrients_by_plants import CoefficientUtilizationNutrientsByPlants
from swagger_client.models.culture import Culture
from swagger_client.models.culture_to_disease import CultureToDisease
from swagger_client.models.damage_area import DamageArea
from swagger_client.models.degree_of_soil_moisture import DegreeOfSoilMoisture
from swagger_client.models.depth_of_arable_layer import DepthOfArableLayer
from swagger_client.models.determinant import Determinant
from swagger_client.models.determinant_disease import DeterminantDisease
from swagger_client.models.determinant_progress import DeterminantProgress
from swagger_client.models.disease import Disease
from swagger_client.models.disease_group import DiseaseGroup
from swagger_client.models.disease_subgroup import DiseaseSubgroup
from swagger_client.models.disease_to_damage_area import DiseaseToDamageArea
from swagger_client.models.fed_calculator import FedCalculator
from swagger_client.models.fedcalculator_create_calculator import FedcalculatorCreateCalculator
from swagger_client.models.fedcalculator_set_parameters import FedcalculatorSetParameters
from swagger_client.models.fertilizer_action_year import FertilizerActionYear
from swagger_client.models.fertilizer_group import FertilizerGroup
from swagger_client.models.fertilizer_main_drug import FertilizerMainDrug
from swagger_client.models.fertilizer_main_drug_synonyms import FertilizerMainDrugSynonyms
from swagger_client.models.fertilizer_registrant import FertilizerRegistrant
from swagger_client.models.fertilizer_release_form import FertilizerReleaseForm
from swagger_client.models.fertilizer_seller import FertilizerSeller
from swagger_client.models.fertilizer_soil_type import FertilizerSoilType
from swagger_client.models.fertilizer_subgroup import FertilizerSubgroup
from swagger_client.models.fertilizer_to_main_drug import FertilizerToMainDrug
from swagger_client.models.fertilizer_to_registration import FertilizerToRegistration
from swagger_client.models.fertilizer_to_seller import FertilizerToSeller
from swagger_client.models.fertilizer_trade_name import FertilizerTradeName
from swagger_client.models.fertilizer_type import FertilizerType
from swagger_client.models.fluid_calculator import FluidCalculator
from swagger_client.models.fluid_calculator_calculation_parameters_dto_serializer_ import FluidCalculatorCalculationParametersDtoSerializer_
from swagger_client.models.fluid_calculator_detail import FluidCalculatorDetail
from swagger_client.models.fluid_consumption_rate_through_nozzle import FluidConsumptionRateThroughNozzle
from swagger_client.models.fluidcalculator_create_calculator import FluidcalculatorCreateCalculator
from swagger_client.models.fluidcalculator_set_calculation_parameters import FluidcalculatorSetCalculationParameters
from swagger_client.models.fluidcalculator_set_plant_protection import FluidcalculatorSetPlantProtection
from swagger_client.models.harmful_object import HarmfulObject
from swagger_client.models.hazard_class import HazardClass
from swagger_client.models.mechanical_composition_of_soil import MechanicalCompositionOfSoil
from swagger_client.models.microorganisms_genus import MicroorganismsGenus
from swagger_client.models.microorganisms_genus_dto_serializer_ import MicroorganismsGenusDtoSerializer_
from swagger_client.models.mycobiota_type import MycobiotaType
from swagger_client.models.mycological_calculator import MycologicalCalculator
from swagger_client.models.mycological_calculator_detail import MycologicalCalculatorDetail
from swagger_client.models.mycologicalcalculator_create_calculator import MycologicalcalculatorCreateCalculator
from swagger_client.models.mycologicalcalculator_set_parameters import MycologicalcalculatorSetParameters
from swagger_client.models.normative_calculator import NormativeCalculator
from swagger_client.models.normative_calculator_acidity_group import NormativeCalculatorAcidityGroup
from swagger_client.models.normative_calculator_culture import NormativeCalculatorCulture
from swagger_client.models.normative_calculator_detail import NormativeCalculatorDetail
from swagger_client.models.normative_calculator_feeding_plan_dto_serializer_ import NormativeCalculatorFeedingPlanDtoSerializer_
from swagger_client.models.normative_calculator_fertilizer_detail import NormativeCalculatorFertilizerDetail
from swagger_client.models.normative_calculator_fertilizer_dto_serializer_ import NormativeCalculatorFertilizerDtoSerializer_
from swagger_client.models.normative_calculator_fertilizer_type import NormativeCalculatorFertilizerType
from swagger_client.models.normative_calculator_parameters_dto_serializer_ import NormativeCalculatorParametersDtoSerializer_
from swagger_client.models.normative_calculator_preceding_culture import NormativeCalculatorPrecedingCulture
from swagger_client.models.normative_calculator_preceding_culture_category import NormativeCalculatorPrecedingCultureCategory
from swagger_client.models.normative_calculator_region import NormativeCalculatorRegion
from swagger_client.models.normative_calculator_region_culture_combination_view import NormativeCalculatorRegionCultureCombinationView
from swagger_client.models.normativecalculator_create_calculator import NormativecalculatorCreateCalculator
from swagger_client.models.normativecalculator_set_calculation_parameters import NormativecalculatorSetCalculationParameters
from swagger_client.models.normativecalculator_set_feeding_plan import NormativecalculatorSetFeedingPlan
from swagger_client.models.normativecalculator_set_fertilizer import NormativecalculatorSetFertilizer
from swagger_client.models.nozzle_color import NozzleColor
from swagger_client.models.nozzle_pressure import NozzlePressure
from swagger_client.models.paginated_agrochemical_calculator_list import PaginatedAgrochemicalCalculatorList
from swagger_client.models.paginated_application_area_list import PaginatedApplicationAreaList
from swagger_client.models.paginated_causative_agent_list import PaginatedCausativeAgentList
from swagger_client.models.paginated_chemical_class_list import PaginatedChemicalClassList
from swagger_client.models.paginated_culture_list import PaginatedCultureList
from swagger_client.models.paginated_culture_to_disease_list import PaginatedCultureToDiseaseList
from swagger_client.models.paginated_damage_area_list import PaginatedDamageAreaList
from swagger_client.models.paginated_degree_of_soil_moisture_list import PaginatedDegreeOfSoilMoistureList
from swagger_client.models.paginated_depth_of_arable_layer_list import PaginatedDepthOfArableLayerList
from swagger_client.models.paginated_determinant_list import PaginatedDeterminantList
from swagger_client.models.paginated_determinant_progress_list import PaginatedDeterminantProgressList
from swagger_client.models.paginated_disease_group_list import PaginatedDiseaseGroupList
from swagger_client.models.paginated_disease_list import PaginatedDiseaseList
from swagger_client.models.paginated_disease_subgroup_list import PaginatedDiseaseSubgroupList
from swagger_client.models.paginated_disease_to_damage_area_list import PaginatedDiseaseToDamageAreaList
from swagger_client.models.paginated_fed_calculator_list import PaginatedFedCalculatorList
from swagger_client.models.paginated_fertilizer_action_year_list import PaginatedFertilizerActionYearList
from swagger_client.models.paginated_fertilizer_group_list import PaginatedFertilizerGroupList
from swagger_client.models.paginated_fertilizer_main_drug_list import PaginatedFertilizerMainDrugList
from swagger_client.models.paginated_fertilizer_main_drug_synonyms_list import PaginatedFertilizerMainDrugSynonymsList
from swagger_client.models.paginated_fertilizer_release_form_list import PaginatedFertilizerReleaseFormList
from swagger_client.models.paginated_fertilizer_subgroup_list import PaginatedFertilizerSubgroupList
from swagger_client.models.paginated_fertilizer_to_main_drug_list import PaginatedFertilizerToMainDrugList
from swagger_client.models.paginated_fertilizer_to_registration_list import PaginatedFertilizerToRegistrationList
from swagger_client.models.paginated_fertilizer_to_seller_list import PaginatedFertilizerToSellerList
from swagger_client.models.paginated_fertilizer_trade_name_list import PaginatedFertilizerTradeNameList
from swagger_client.models.paginated_fertilizer_type_list import PaginatedFertilizerTypeList
from swagger_client.models.paginated_fluid_calculator_list import PaginatedFluidCalculatorList
from swagger_client.models.paginated_fluid_consumption_rate_through_nozzle_list import PaginatedFluidConsumptionRateThroughNozzleList
from swagger_client.models.paginated_harmful_object_list import PaginatedHarmfulObjectList
from swagger_client.models.paginated_hazard_class_list import PaginatedHazardClassList
from swagger_client.models.paginated_mechanical_composition_of_soil_list import PaginatedMechanicalCompositionOfSoilList
from swagger_client.models.paginated_microorganisms_genus_list import PaginatedMicroorganismsGenusList
from swagger_client.models.paginated_mycobiota_type_list import PaginatedMycobiotaTypeList
from swagger_client.models.paginated_mycological_calculator_list import PaginatedMycologicalCalculatorList
from swagger_client.models.paginated_normative_calculator_acidity_group_list import PaginatedNormativeCalculatorAcidityGroupList
from swagger_client.models.paginated_normative_calculator_list import PaginatedNormativeCalculatorList
from swagger_client.models.paginated_normative_calculator_preceding_culture_category_list import PaginatedNormativeCalculatorPrecedingCultureCategoryList
from swagger_client.models.paginated_normative_calculator_preceding_culture_list import PaginatedNormativeCalculatorPrecedingCultureList
from swagger_client.models.paginated_normative_calculator_region_culture_combination_view_list import PaginatedNormativeCalculatorRegionCultureCombinationViewList
from swagger_client.models.paginated_nozzle_color_list import PaginatedNozzleColorList
from swagger_client.models.paginated_nozzle_pressure_list import PaginatedNozzlePressureList
from swagger_client.models.paginated_place_of_production_list import PaginatedPlaceOfProductionList
from swagger_client.models.paginated_plant_protection_group_list import PaginatedPlantProtectionGroupList
from swagger_client.models.paginated_plant_protection_main_drug_list import PaginatedPlantProtectionMainDrugList
from swagger_client.models.paginated_plant_protection_product_application_list import PaginatedPlantProtectionProductApplicationList
from swagger_client.models.paginated_plant_protection_product_list import PaginatedPlantProtectionProductList
from swagger_client.models.paginated_preparative_form_list import PaginatedPreparativeFormList
from swagger_client.models.paginated_rb_calculator_list import PaginatedRbCalculatorList
from swagger_client.models.paginated_rb_calculator_region_culture_combination_view_list import PaginatedRbCalculatorRegionCultureCombinationViewList
from swagger_client.models.paginated_region_list import PaginatedRegionList
from swagger_client.models.paginated_registrant_list import PaginatedRegistrantList
from swagger_client.models.paginated_rosselkhoz_bank_agrochemical_analysis_request_list import PaginatedRosselkhozBankAgrochemicalAnalysisRequestList
from swagger_client.models.paginated_rosselkhoz_bank_complex_analysis_request_list import PaginatedRosselkhozBankComplexAnalysisRequestList
from swagger_client.models.paginated_season_scheme_list import PaginatedSeasonSchemeList
from swagger_client.models.paginated_seller_list import PaginatedSellerList
from swagger_client.models.paginated_soil_sampling_depth_list import PaginatedSoilSamplingDepthList
from swagger_client.models.paginated_soil_type_list import PaginatedSoilTypeList
from swagger_client.models.paginated_treatment_type_list import PaginatedTreatmentTypeList
from swagger_client.models.paginated_unit_of_measurement_list import PaginatedUnitOfMeasurementList
from swagger_client.models.paginated_user_list import PaginatedUserList
from swagger_client.models.password_reset_confirm import PasswordResetConfirm
from swagger_client.models.patched_teleagronom_user import PatchedTeleagronomUser
from swagger_client.models.patched_user import PatchedUser
from swagger_client.models.place_of_production import PlaceOfProduction
from swagger_client.models.plant_protection_culture import PlantProtectionCulture
from swagger_client.models.plant_protection_group import PlantProtectionGroup
from swagger_client.models.plant_protection_main_drug import PlantProtectionMainDrug
from swagger_client.models.plant_protection_product import PlantProtectionProduct
from swagger_client.models.plant_protection_product_application import PlantProtectionProductApplication
from swagger_client.models.plant_protection_product_application_to_culture import PlantProtectionProductApplicationToCulture
from swagger_client.models.plant_protection_product_application_to_harmful_object import PlantProtectionProductApplicationToHarmfulObject
from swagger_client.models.plant_protection_product_for_application import PlantProtectionProductForApplication
from swagger_client.models.plant_protection_product_to_application_area import PlantProtectionProductToApplicationArea
from swagger_client.models.plant_protection_product_to_chemical_class import PlantProtectionProductToChemicalClass
from swagger_client.models.plant_protection_product_to_main_drug import PlantProtectionProductToMainDrug
from swagger_client.models.plant_protection_product_to_registration import PlantProtectionProductToRegistration
from swagger_client.models.plant_protection_product_to_seller import PlantProtectionProductToSeller
from swagger_client.models.plant_protection_registrant import PlantProtectionRegistrant
from swagger_client.models.plant_protection_seller import PlantProtectionSeller
from swagger_client.models.plant_protection_unit_of_measurement import PlantProtectionUnitOfMeasurement
from swagger_client.models.preparative_form import PreparativeForm
from swagger_client.models.rb_calculator import RbCalculator
from swagger_client.models.rb_calculator_culture import RbCalculatorCulture
from swagger_client.models.rb_calculator_detail import RbCalculatorDetail
from swagger_client.models.rb_calculator_fertilizer_detail import RbCalculatorFertilizerDetail
from swagger_client.models.rb_calculator_fertilizer_dto_serializer_ import RbCalculatorFertilizerDtoSerializer_
from swagger_client.models.rb_calculator_fertilizer_feeding_plan_dto_serializer_ import RbCalculatorFertilizerFeedingPlanDtoSerializer_
from swagger_client.models.rb_calculator_fertilizer_type import RbCalculatorFertilizerType
from swagger_client.models.rb_calculator_parameters_dto_serializer_ import RbCalculatorParametersDtoSerializer_
from swagger_client.models.rb_calculator_region import RbCalculatorRegion
from swagger_client.models.rb_calculator_region_culture_combination_view import RbCalculatorRegionCultureCombinationView
from swagger_client.models.rb_calculator_report_dto_serializer_ import RbCalculatorReportDtoSerializer_
from swagger_client.models.rbcalculator_create_calculator import RbcalculatorCreateCalculator
from swagger_client.models.rbcalculator_set_calculation_parameters import RbcalculatorSetCalculationParameters
from swagger_client.models.rbcalculator_set_feeding_plan import RbcalculatorSetFeedingPlan
from swagger_client.models.rbcalculator_set_fertilizer import RbcalculatorSetFertilizer
from swagger_client.models.reanswer_question import ReanswerQuestion
from swagger_client.models.region import Region
from swagger_client.models.registrant import Registrant
from swagger_client.models.rosselkhoz_bank_agrochemical_analysis_request import RosselkhozBankAgrochemicalAnalysisRequest
from swagger_client.models.rosselkhoz_bank_agrochemical_calculator_detail import RosselkhozBankAgrochemicalCalculatorDetail
from swagger_client.models.rosselkhoz_bank_complex_analysis_request import RosselkhozBankComplexAnalysisRequest
from swagger_client.models.rosselkhoz_bank_create_agrochemical_analysis_request_command import RosselkhozBankCreateAgrochemicalAnalysisRequestCommand
from swagger_client.models.rosselkhoz_bank_create_complex_analysis_request_command import RosselkhozBankCreateComplexAnalysisRequestCommand
from swagger_client.models.rosselkhoz_bank_set_delivery_method_for_agrochemical_analysis_request_command import RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand
from swagger_client.models.season_scheme import SeasonScheme
from swagger_client.models.seller import Seller
from swagger_client.models.send_email_reset import SendEmailReset
from swagger_client.models.set_password import SetPassword
from swagger_client.models.set_username import SetUsername
from swagger_client.models.soil_sampling_depth import SoilSamplingDepth
from swagger_client.models.soil_type import SoilType
from swagger_client.models.teleagronom_user import TeleagronomUser
from swagger_client.models.token_obtain_pair import TokenObtainPair
from swagger_client.models.token_refresh import TokenRefresh
from swagger_client.models.token_verify import TokenVerify
from swagger_client.models.treatment_type import TreatmentType
from swagger_client.models.unit_of_measurement import UnitOfMeasurement
from swagger_client.models.user import User
from swagger_client.models.user_create import UserCreate
from swagger_client.models.username_reset_confirm import UsernameResetConfirm
