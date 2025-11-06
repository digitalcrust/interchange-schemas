# Spots ↔ Checkins Quick Reference (Expanded)

This doc shows **requests**, **response status**, and **example response bodies** for:

- `POST https://dev.macrostrat.org/api/v3/dev/interchange-data/spot-to-fieldsite`
- `POST https://dev.macrostrat.org/api/v3/dev/interchange-data/fieldsite-to-checkin`
- `POST https://dev.macrostrat.org/api/v3/dev/interchange-data/spot-to-checkin`

Each endpoint includes **single** and **multiple** request body variants. Long JSON examples are hidden under expandable sections.

---

## POST `/interchange-data/spot-to-fieldsite`

Converts StraboSpot **FeatureCollection(s)** → list of `FieldSite` objects.

### Single FeatureCollection (one or many Point features)
<details>
<summary>Request body (FeatureCollection)</summary>

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -97.676182,
              38.578769
            ],
            [
              -97.674251,
              38.579943
            ],
            [
              -97.6735,
              38.578198
            ],
            [
              -97.676182,
              38.578769
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:43.000Z",
        "name": "Abc126",
        "time": "2022-08-10T16:30:43.000Z",
        "id": 16601490430653,
        "modified_timestamp": 1660149043065,
        "self": "https://strabospot.org/db/feature/16601490430653"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            -97.679658,
            38.578886
          ],
          [
            -97.674508,
            38.576907
          ],
          [
            -97.671762,
            38.578484
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:34.000Z",
        "name": "Abc125",
        "time": "2022-08-10T16:30:34.000Z",
        "id": 16601490340852,
        "modified_timestamp": 1660149034086,
        "self": "https://strabospot.org/db/feature/16601490340852"
      },
      "type": "Feature"
    },
    {
      "properties": {
        "images": [
          {
            "width": 4032,
            "caption": "Image description here",
            "id": 16530015128805,
            "title": "My image",
            "annotated": true,
            "height": 3024,
            "image_type": "photo",
            "self": "https://strabospot.org/db/image/16530015128805"
          }
        ],
        "date": "2022-06-19T22:27:11.000Z",
        "altitude": 23,
        "notes": "Spot notes here",
        "data": {
          "urls": [
            "http://www.google.com"
          ]
        },
        "other_features": [
          {
            "id": 16530016041795,
            "label": "OthFeat",
            "type": "hydrologic",
            "name": "Feature Name",
            "description": "Desc here"
          }
        ],
        "orientation_data": [
          {
            "type": "planar_orientation",
            "id": 16529994975257,
            "label": "Plane1",
            "strike": 123,
            "dip_direction": 234,
            "dip": 45,
            "quality": "4",
            "feature_type": "fracture",
            "fracture_type": "opening_mode",
            "fracture_defined_by": "Something",
            "movement": "se_side_up",
            "movement_justification": [
              "not_specified",
              "offset_foliation"
            ],
            "directional_indicators": [
              "riedel_shear",
              "slickenfibers"
            ],
            "thickness": 2,
            "length": 3,
            "notes": "Pl feat notes"
          },
          {
            "type": "linear_orientation",
            "id": 16529995763665,
            "label": "Line1",
            "trend": 12,
            "plunge": 23,
            "rake": 34,
            "rake_calculated": "no",
            "quality": "3",
            "feature_type": "z_fold",
            "defined_by": "Something",
            "notes": "Notes here"
          },
          {
            "type": "tabular_orientation",
            "id": 16529996088030,
            "label": "Tab zone 1",
            "strike": 23,
            "dip_direction": 45,
            "dip": 55,
            "quality": "3",
            "feature_type": "vein",
            "vein_type": "normal_opening",
            "vein_fill": "quartz",
            "thickness": 23,
            "tabularity": "semi_constant",
            "length": 23,
            "defined_by": "Something here",
            "notes": "Tab notes"
          },
          {
            "type": "linear_orientation",
            "id": 16590144068585,
            "label": "Line2",
            "trend": 44,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144221415,
            "label": "line3",
            "trend": 55,
            "plunge": 66,
            "rake": 77,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144415915,
            "label": "line4",
            "trend": 11,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          }
        ],
        "modified_timestamp": 1660148979966,
        "_3d_structures": [
          {
            "type": "fabric",
            "id": 16529996735747,
            "feature_type": "tectonite",
            "tectonite_type": "sl_tectonite",
            "tectonite_character": "s___l",
            "struct_notes": "Fab notes",
            "label": "tectonite"
          },
          {
            "type": "tensor",
            "id": 16529997746294,
            "label": "Tensor1",
            "feature_type": "non_ellipsoidal_data",
            "non_ellipsoidal_type": "flow_apophyses",
            "nonellipsoidal_max_value": 23,
            "nonellipsoidal_max_value_uncer": 43,
            "nonellipsoidal_max_trend": 56,
            "nonellipsoidal_max_trend_uncer": 34,
            "nonellipsoidal_max_plunge": 23,
            "nonellipsoidal_max_plunge_unce": 54,
            "nonellipsoidal_int_value": 23,
            "nonellipsoidal_int_value_uncer": 32,
            "nonellipsoidal_int_trend": 45,
            "nonellipsoidal_int_uncertainty": 34,
            "nonellipsoidal_int_plunge": 56,
            "nonellipsoidal_int_plunge_unce": 34,
            "nonellipsoidal_min_value": 23,
            "nonellipsoidal_min_value_uncer": 45,
            "nonellipsoidal_min_trend": 23,
            "nonellipsoidal_min_trend_uncer": 32,
            "nonellipsoidal_min_plunge": 23,
            "nonellipsoidal_min_plunge_unce": 45,
            "non_ellipsoidal_tensor_notes": "Notes here",
            "nonellipsoidal_quality_of_meas": "4",
            "struct_notes": "Tensor notes"
          },
          {
            "type": "other",
            "id": 16529998349655,
            "label": "Other1",
            "feature_type": "boudinage",
            "boudinage_geometry": "unidirectional",
            "boudinage_shape": "symmetrical",
            "boudinage_competent": "Mat",
            "boudinage_incompetent": "Mat",
            "average_width_of_boudin_neck": 34,
            "number_of_necks_measured": 3,
            "boudinage_wavelength_m": 4,
            "boudinaged_layer_thickness_m": 6,
            "boudinage_strike": 23,
            "boudinage_dip_direction": 34,
            "boudinage_dip": 56,
            "boudinage_trend": 23,
            "boudinage_plunge": 43,
            "boudinage_trend_uncertainty": 32,
            "boudinage_2nd_trend": 23,
            "boudinage_2nd_plunge": 34,
            "boudinage_2nd_trend_uncertaint": 12,
            "struct_notes": "Notes"
          },
          {
            "type": "fold",
            "id": 16529996884051,
            "label": "Fold1",
            "feature_type": "monocline",
            "Trend": 23,
            "Plunge": 34,
            "Linearity": "4",
            "Measurement_Quality": "4",
            "Strike": 12,
            "Azimuthal_Dip_Direction": 34,
            "Dip": 32,
            "Planarity": "3",
            "Measurement_Quality_001": "5___excellent",
            "fold_attitude": "vertical",
            "fold_shape": "class_1b__para",
            "tightness": "tight",
            "Hinge_Shape": "subrounded",
            "vergence": "south",
            "wavelength_m": 12,
            "amplitude_m": 23,
            "competent_material_fold": "Mat here",
            "folded_layer_thickness_m": 55,
            "incompetent_material_fold": "Mat here",
            "fold_fol_strike": 12,
            "fold_fol_dip_direction": 23,
            "fold_fol_dip": 34,
            "fold_fol_quality": "approximate",
            "fold_foliation_Type": "axial_planar",
            "fold_foliation_description": "Desc here",
            "fold_notes": "Fold notes here"
          }
        ],
        "fabrics": [
          {
            "type": "fault_rock",
            "id": 16530036019286,
            "label": "Fabric1",
            "inco_nofol": "fault_breccia",
            "inco_nofo_char": "Fab",
            "inco_fol": "foliated_gouge",
            "inco_fo_char": "Fab",
            "co_nofol": "cata",
            "co_nofo_char": "Fab",
            "co_fol": "fol_ultracata",
            "tectonite_type": "s>>l",
            "co_fo_char": "Fab",
            "structural_fabric": [
              "folding",
              "comp_banding"
            ],
            "char_fold": "Fold",
            "comp_band_min": "Zen",
            "spatial_config": [
              "planar",
              "anastomosing"
            ],
            "desc_spat_char": "Desc",
            "kin_ind_present": "yes_kin",
            "kinematic_fab": [
              "oblique_fabric",
              "asymm_fold"
            ],
            "grain_shape_char": "Zrn",
            "asym_fold_char": "Char",
            "sense_of_shear": "Top",
            "interp_note": "Notes"
          },
          {
            "type": "igneous_rock",
            "id": 16530036980941,
            "label": "Fabric2",
            "planar_fab": [
              "no_p_fab",
              "other_p_fab"
            ],
            "lin_fab": [
              "none"
            ],
            "mag_tectonite": "l>s",
            "add_mag_fab": [
              "commingle",
              "mullions"
            ],
            "mag_commingle": "Comm",
            "mag_mullion": "Mull",
            "magmatic_str": [
              "no_mag_str",
              "plume_str"
            ],
            "solid_state_str": [
              "ss_fab",
              "anneal_sz"
            ],
            "char_ss_fab": "Sol",
            "char_ss_sz": "Shear",
            "addition_fab": [
              "structural",
              "other"
            ],
            "str_fab": [
              "folding",
              "fractures"
            ],
            "fold_char": "Fold",
            "fracture_char": "Frac",
            "other_fab_char": "Other",
            "ss_tectonite": "ls",
            "mag_interp_note": "Notes"
          },
          {
            "type": "metamorphic_rock",
            "id": 16530037849501,
            "label": "Fabric3",
            "grain_size": "medium",
            "planar_fabric": [
              "gneissic_band",
              "schistosity"
            ],
            "plan_fab_min_1": "Min",
            "plan_fab_min_2": "Min",
            "plan_fab_min_3": "Min",
            "plan_fab_min_4": "Min",
            "spatial_var": "domainal",
            "length_scale": "Scale",
            "linear_fab": [
              "min_align_lin",
              "intersect_lin"
            ],
            "int_lin_char": "Planes",
            "other_met_fab": [
              "metasom",
              "migmatite"
            ],
            "metasomatic": "Min",
            "migmatitic": "Min",
            "additional_fab": [
              "structural",
              "relict_sed"
            ],
            "structural_fab": [
              "folding",
              "fault"
            ],
            "char_folding": "Char",
            "char_fault": "Char",
            "relict_sed_fab": [
              "bed",
              "flow_top_brecc"
            ],
            "kinematic_ind": "kin_yes",
            "kinematic_fab": [
              "asymm_fold",
              "bookshelf_slip",
              "sigmoidal_gash"
            ],
            "asym_fold_char": "Char",
            "book_slip_char": "Char",
            "sig_gash_char": "Char",
            "sense_of_shear": "Sense here",
            "tectonite_type": "ls",
            "p_t_d_history": "Hist here",
            "interp_note_meta": "Notes"
          }
        ],
        "sed": {
          "strat_section": {
            "strat_section_id": 16530017020988,
            "column_profile": "clastic",
            "column_y_axis_units": "m",
            "section_well_name": "Sec name here",
            "misc_labels": true,
            "display_lithology_patterns": true,
            "section_type": "core",
            "what_core_repository": "Repo here",
            "type_of_corer": "Corer type here",
            "depth_from_surface_to_start_of": "3",
            "total_core_length": "123",
            "location_locality": "Some locality here",
            "basin": "Some basin here",
            "age": "12345",
            "purpose": [
              "geochronology",
              "sequence_strat",
              "pleasure"
            ],
            "project_description": "Desc",
            "dates_of_work": "Dates here",
            "scale_of_interest": [
              "single_basin",
              "single_outcrop",
              "multi_basins",
              "single_core"
            ],
            "obs_interval_bed_obs_scale": "dm",
            "how_is_section_georeferenced": "point_at_secti",
            "strat_section_notes": "Some notes here"
          },
          "character": "package_succe",
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "mudstone",
              "mud_silt_grain_size": "clay",
              "relative_resistance_weather": "1",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "color_appearance": [
                "uniform",
                "patchy",
                "striped"
              ],
              "notes": "Notes here",
              "sand_grain_size": "sand_fine_low",
              "grain_size_range": [
                "sand_fine_low",
                "pebble",
                "pebble",
                "sand_medium_l"
              ],
              "congl_grain_size": "pebble",
              "breccia_grain_size": "pebble",
              "sand_fine_lower_percent": 12,
              "sand_medium_lower_percent": 23,
              "pebble_percent": 34,
              "maximum_clast_size_cm": 12,
              "minimum_clast_size_cm": 23,
              "average_clast_size_cm": 34,
              "matrix_size": [
                "silt",
                "none"
              ],
              "character": [
                "matrix-support",
                "imbrication"
              ],
              "sorting": [
                "well_sorted",
                "mod_sorted"
              ],
              "rounding": [
                "rounded",
                "very_angular"
              ],
              "shape": [
                "spherical",
                "equant"
              ],
              "minerals_present": [
                "quartz",
                "halite",
                "calcite",
                "chert",
                "rip_up_clasts"
              ],
              "sandstone_type_dott": [
                "quartz_arenite",
                "arkosic_arenit"
              ],
              "sandstone_type_folk_mcbride": [
                "quartzarenite",
                "subarkose",
                "sublitharenite"
              ],
              "sandstone_modifier": [
                "rip_up_clasts",
                "wood"
              ],
              "skeletal_carbonate_components": [
                "mollusc",
                "calcareous_alg",
                "brachiopod"
              ],
              "mollusc_percent": 12,
              "brachiopod_percent": 23,
              "calcareous_algae_percent": 34,
              "non_skeletal_carbonate_compone": [
                "mud",
                "oncoid",
                "pisoid"
              ],
              "mud_percent": 12,
              "oncoid_percent": 23,
              "pisoid_percent": 34,
              "clay_or_mudstone_type": [
                "red_mudstone",
                "siliceous_calc"
              ],
              "siliceous_calcareous_mudstone_percent": 12,
              "red_mudstone_percent": 23,
              "conglomerate_composition": [
                "extraformation",
                "monomictic"
              ],
              "clast_composition": [
                "igneous_clast",
                "conglomerate",
                "schist"
              ],
              "conglomerate_clast_percent": 12,
              "matrix_composition": [
                "conglomerate",
                "extrusive_igneous"
              ],
              "extrusive_igneous_matrix_percent": 23,
              "conglomerate_matrix_percent": 34,
              "volcaniclastic_type": [
                "glass"
              ],
              "glass_percent": 12,
              "evaporite_type": [
                "gyp_anhyd_dia"
              ],
              "gypsum_anhydrite_diagenetic_percent": 12,
              "gypsum_anhydrite_diagenetic_type": [
                "nodular_to_chi",
                "displacive"
              ],
              "phosphorite_type": [
                "nodular"
              ],
              "organic_coal_lithologies": [
                "peat",
                "coal_ball"
              ],
              "peat_percent": 12,
              "coal_ball_percent": 23
            }
          ],
          "bedding": {
            "thickness_of_individual_beds": 12,
            "package_bedding_trends": "uniform",
            "beds": [
              {
                "package_geometry": [
                  "discontinuous",
                  "tabular_parall"
                ],
                "shape_of_lower_contacts": [
                  "flat",
                  "irregular"
                ],
                "character_of_lower_contacts": [
                  "flat",
                  "undulatory"
                ],
                "shape_of_upper_contacts": [
                  "undulatory",
                  "curved"
                ],
                "character_of_upper_contacts": [
                  "sharp",
                  "gradational"
                ],
                "upper_contact_relief": "Relief here",
                "notes": "Notes here"
              }
            ]
          },
          "structures": [
            {
              "massive_structureless": "yes",
              "cross_bedding_type": [
                "cross_bedding",
                "trough"
              ],
              "cross_bedding_height_cm": 12,
              "cross_bedding_width_cm": 23,
              "cross_bedding_thickness_cm": 34,
              "cross_bedding_spacing_cm": 45,
              "ripple_lamination_type": [
                "cross_lamin",
                "lenticular"
              ],
              "ripple_lamination_height_mm": 12,
              "ripple_lamination_width_mm": 23,
              "ripple_lamination_thick_mm": 23,
              "ripple_lamination_spacing_mm": 34,
              "horizontal_bedding_type": [
                "horizontal",
                "planar"
              ],
              "graded_bedding_type": "normally_grade",
              "deformation_structures": [
                "contorted_bedd",
                "dikes"
              ],
              "lag_type": [
                "lag_deposit",
                "rip_up_clasts"
              ],
              "clast_composition": "Comp",
              "clast_size": "12",
              "layer_thickness_shape": "23",
              "other_common_structures": [
                "bouma_sequence"
              ],
              "bouma_sequence_part": [
                "a"
              ],
              "notes": "Notes here",
              "bioturbation_index": "1_sparse",
              "bedding_plane_features": [
                "bedforms",
                "gutter_cast"
              ],
              "bedding_plane_features_scale": "12",
              "bedform_type": [
                "wave_ripples",
                "3d_crests",
                "ladderback"
              ],
              "bedding_plane_features_orientation": "12",
              "bedform_scale": "23",
              "crest_orientation_azimuth_0_360": "45",
              "paleosol_horizons": [
                "o",
                "c"
              ],
              "o_horizon_thickness_cm": 12,
              "c_horizon_thickness_cm": 23,
              "paleosol_structures": [
                "peds",
                "leaching_horiz"
              ],
              "additional_modifiers": "Additional here",
              "paleosol_classification": [
                "gelisol",
                "histosol"
              ]
            }
          ],
          "diagenesis": [
            {
              "cement_composition": [
                "calcite",
                "clay"
              ],
              "vein_type": "parallel",
              "vein_width": 12,
              "vein_length": 23,
              "vein_orientation": "45",
              "vein_mineralogy": "iron_oxides",
              "fracture_type": "oblique",
              "fracture_width": 12,
              "fracture_length": 23,
              "fracture_orientation": "Or",
              "fracture_mineralogy": "evaporite_min",
              "nodules_concretions_size": "mm",
              "min": 12,
              "max": 45,
              "average": 55,
              "nodules_concretions_shape": [
                "spherical",
                "irregular"
              ],
              "spacing": 33,
              "nodules_concretions_type": "layered",
              "nodules_concretions_comp": [
                "calcite",
                "gypsum_anhydri"
              ],
              "replacement_type": "fossil_selecti",
              "recrystallization_type": "local",
              "other_diagenetic_features": [
                "stylolites",
                "liesegang_band"
              ],
              "fabric_selective": [
                "interparticle",
                "intraparticle"
              ],
              "non_selective": [
                "channel",
                "vug"
              ],
              "carbonate_desicc_and_diss": [
                "grykes",
                "sheet_cracks"
              ],
              "notes": "Notes here"
            }
          ],
          "fossils": [
            {
              "invertebrate": [
                "porifera_spong",
                "cnidaria",
                "chordata",
                "mollusca"
              ],
              "mollusca": [
                "cephalopod",
                "belemnite"
              ],
              "chordate": "tunicate",
              "plant_algae": [
                "red_algae",
                "phylloid"
              ],
              "vertebrate": [
                "chondrichthyes",
                "aves"
              ],
              "faunal_assemblage": "heterozoan",
              "diversity": "medium",
              "descriptive": [
                "track",
                "sub_vertical"
              ],
              "burrow_fill_type": [
                "mudstone",
                "active"
              ],
              "behavioral_grouping": [
                "locomotion",
                "farming"
              ],
              "ichnofacies": "skolithos",
              "list_of_specific_types": "Types here",
              "dominant_component": "microbial_reef",
              "other_dominant_component": "Other dom here",
              "microbial_reef_or_skelatal_mic": [
                "micro_laminate",
                "tufa"
              ],
              "other_microbial_or_skeletal_mi": "Other mic here",
              "height": "12",
              "width": "23",
              "orientation_if_elongate_azimu": 45,
              "shape": "dome",
              "type": "fringing",
              "accessory_structures": [
                "fenestrae",
                "geopetal"
              ],
              "notes": "Notes here"
            }
          ],
          "interpretations": [
            {
              "sediment_transport": [
                "waves",
                "turbidity_curr"
              ],
              "fluidization": "liquefaction",
              "miscellaneous": [
                "ice_rafting",
                "desiccation"
              ],
              "notes": "Notes here",
              "general": [
                "continental",
                "transitional"
              ],
              "clastic": [
                "playa",
                "glacial_and_pr"
              ],
              "glacial_and_proglacial_environ": [
                "till",
                "outwash"
              ],
              "carbonates": [
                "factory"
              ],
              "factory": [
                "photozoan",
                "metozoan"
              ],
              "geometry": "undulatory",
              "relief_scale": "cm",
              "extent": "23",
              "extent_scale": "m",
              "relief": "12",
              "type": [
                "mineralization",
                "pedogenic"
              ],
              "stratal_termination": "toplap",
              "general_surfaces": "Gen surf",
              "sequence_stratigraphic_surfaces": "type_3_sequenc",
              "named": "Named here",
              "description": [
                "fining_upward",
                "isolated"
              ],
              "stacking_sequence_stratigraphy": [
                "progradational",
                "highstand_syst"
              ],
              "fluvial_architectural_elements": [
                "gravelly_bar_o",
                "sandy_bedform"
              ],
              "lacustrine_architecture_interpretation": [
                "overfilled",
                "balanced"
              ],
              "carbonate_platform_geometry": [
                "attached",
                "unrimmed_platf"
              ],
              "deep_water_architctural_element": [
                "levee",
                "sheet"
              ],
              "carbonate_margin_geometry": [
                "accretionary_m",
                "other"
              ],
              "other_carbonate_margin_geometry": "Other geometry"
            }
          ]
        },
        "samples": [
          {
            "sample_type": "field",
            "id": 16530015451321,
            "sample_id_name": "Efg345",
            "label": "Sample1",
            "main_sampling_purpose": "geochronology",
            "deposit_thickness": "23",
            "sample_description": "Samp desc here",
            "material_type": "sediment",
            "inplaceness_of_sample": "5___definitely",
            "oriented_sample": "yes",
            "sample_orientation_notes": "Notes here",
            "sample_size": "123",
            "degree_of_weathering": "4",
            "sample_notes": "Some notes"
          }
        ],
        "gps_accuracy": 1.23,
        "name": "Spot1",
        "time": "2022-06-19T22:27:11.000Z",
        "id": 16529992313378,
        "pet": {
          "volcanic_rock_type": [
            "latite"
          ],
          "igneous_rock_class": [
            "volcanic"
          ],
          "rock_type": [
            "igneous"
          ],
          "occurence_volcanic": [
            "dome",
            "unclear"
          ],
          "texture_volcanic": [
            "clastic",
            "aphanitic"
          ],
          "color_index_volc": 23,
          "color_index_source_volc": "strabotools",
          "vol_characteristic_size_of_cry": 123,
          "structure_volcanic": [
            "eutaxitic"
          ],
          "alteration_volcanic": [
            "metamorphic_ov"
          ],
          "notes_volcanic": "Notes here",
          "minerals": [
            {
              "id": 16530034561873,
              "full_mineral_name": "Zircon",
              "mineral_abbrev": "zrn",
              "habit": "acicular",
              "textural_setting_igneous": [
                "phenocryst",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 12,
              "maximum_grain_size_mm": 23,
              "modal": 34,
              "mineral_notes": "Mineral notes here"
            },
            {
              "id": 16530035059185,
              "full_mineral_name": "Aegirine",
              "mineral_abbrev": "aeg",
              "habit": "euhedral",
              "textural_setting_igneous": [
                "vesicle",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 1,
              "maximum_grain_size_mm": 2,
              "modal": 3,
              "mineral_notes": "Notes here"
            }
          ],
          "reactions": [
            {
              "id": 16530035338583,
              "reactions": "Ab=zn+bc",
              "based_on": [
                "corona",
                "mineral_degrad"
              ],
              "notes": "Notes here"
            }
          ]
        },
        "spot_radius": 1.3,
        "self": "https://strabospot.org/db/feature/16529992313378"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -97.679878,
          38.576911
        ]
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0,
              0
            ],
            [
              0,
              80
            ],
            [
              20,
              80
            ],
            [
              20,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-05-19T23:11:15.000Z",
        "altitude": 405.94,
        "lng": -97.679578,
        "strat_section_id": 16530017020988,
        "surface_feature": {
          "surface_feature_type": "strat_interval"
        },
        "modified_timestamp": 1653001875459,
        "sed": {
          "character": "bed",
          "interval": {
            "interval_thickness": 4,
            "thickness_units": "m"
          },
          "bedding": {
            "beds": [
              {
                "notes": "Notes here"
              }
            ]
          },
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "siltstone",
              "mud_silt_grain_size": "silt",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "relative_resistance_weather": "3",
              "notes": "Notes here"
            }
          ]
        },
        "name": "Abc123",
        "time": "2022-05-19T23:11:15.000Z",
        "id": 16530018754410,
        "lat": 38.577,
        "self": "https://strabospot.org/db/feature/16530018754410"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Point",
        "coordinates": [
          2705.0625,
          1775.8125
        ]
      },
      "properties": {
        "date": "2022-08-10T16:29:43.000Z",
        "lng": -97.679878,
        "image_basemap": 16530015128805,
        "name": "On image",
        "time": "2022-08-10T16:29:43.000Z",
        "id": 16601489837307,
        "lat": 38.576911,
        "modified_timestamp": 1660148995221,
        "self": "https://strabospot.org/db/feature/16601489837307"
      },
      "type": "Feature"
    }
  ]
}

```
</details>

### Multiple FeatureCollections (array)
<details>
<summary>Request body ([FeatureCollection, ...])</summary>

```json
[{
  "type": "FeatureCollection",
  "features": [
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -97.676182,
              38.578769
            ],
            [
              -97.674251,
              38.579943
            ],
            [
              -97.6735,
              38.578198
            ],
            [
              -97.676182,
              38.578769
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:43.000Z",
        "name": "Abc126",
        "time": "2022-08-10T16:30:43.000Z",
        "id": 16601490430653,
        "modified_timestamp": 1660149043065,
        "self": "https://strabospot.org/db/feature/16601490430653"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            -97.679658,
            38.578886
          ],
          [
            -97.674508,
            38.576907
          ],
          [
            -97.671762,
            38.578484
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:34.000Z",
        "name": "Abc125",
        "time": "2022-08-10T16:30:34.000Z",
        "id": 16601490340852,
        "modified_timestamp": 1660149034086,
        "self": "https://strabospot.org/db/feature/16601490340852"
      },
      "type": "Feature"
    },
    {
      "properties": {
        "images": [
          {
            "width": 4032,
            "caption": "Image description here",
            "id": 16530015128805,
            "title": "My image",
            "annotated": true,
            "height": 3024,
            "image_type": "photo",
            "self": "https://strabospot.org/db/image/16530015128805"
          }
        ],
        "date": "2022-06-19T22:27:11.000Z",
        "altitude": 23,
        "notes": "Spot notes here",
        "data": {
          "urls": [
            "http://www.google.com"
          ]
        },
        "other_features": [
          {
            "id": 16530016041795,
            "label": "OthFeat",
            "type": "hydrologic",
            "name": "Feature Name",
            "description": "Desc here"
          }
        ],
        "orientation_data": [
          {
            "type": "planar_orientation",
            "id": 16529994975257,
            "label": "Plane1",
            "strike": 123,
            "dip_direction": 234,
            "dip": 45,
            "quality": "4",
            "feature_type": "fracture",
            "fracture_type": "opening_mode",
            "fracture_defined_by": "Something",
            "movement": "se_side_up",
            "movement_justification": [
              "not_specified",
              "offset_foliation"
            ],
            "directional_indicators": [
              "riedel_shear",
              "slickenfibers"
            ],
            "thickness": 2,
            "length": 3,
            "notes": "Pl feat notes"
          },
          {
            "type": "linear_orientation",
            "id": 16529995763665,
            "label": "Line1",
            "trend": 12,
            "plunge": 23,
            "rake": 34,
            "rake_calculated": "no",
            "quality": "3",
            "feature_type": "z_fold",
            "defined_by": "Something",
            "notes": "Notes here"
          },
          {
            "type": "tabular_orientation",
            "id": 16529996088030,
            "label": "Tab zone 1",
            "strike": 23,
            "dip_direction": 45,
            "dip": 55,
            "quality": "3",
            "feature_type": "vein",
            "vein_type": "normal_opening",
            "vein_fill": "quartz",
            "thickness": 23,
            "tabularity": "semi_constant",
            "length": 23,
            "defined_by": "Something here",
            "notes": "Tab notes"
          },
          {
            "type": "linear_orientation",
            "id": 16590144068585,
            "label": "Line2",
            "trend": 44,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144221415,
            "label": "line3",
            "trend": 55,
            "plunge": 66,
            "rake": 77,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144415915,
            "label": "line4",
            "trend": 11,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          }
        ],
        "modified_timestamp": 1660148979966,
        "_3d_structures": [
          {
            "type": "fabric",
            "id": 16529996735747,
            "feature_type": "tectonite",
            "tectonite_type": "sl_tectonite",
            "tectonite_character": "s___l",
            "struct_notes": "Fab notes",
            "label": "tectonite"
          },
          {
            "type": "tensor",
            "id": 16529997746294,
            "label": "Tensor1",
            "feature_type": "non_ellipsoidal_data",
            "non_ellipsoidal_type": "flow_apophyses",
            "nonellipsoidal_max_value": 23,
            "nonellipsoidal_max_value_uncer": 43,
            "nonellipsoidal_max_trend": 56,
            "nonellipsoidal_max_trend_uncer": 34,
            "nonellipsoidal_max_plunge": 23,
            "nonellipsoidal_max_plunge_unce": 54,
            "nonellipsoidal_int_value": 23,
            "nonellipsoidal_int_value_uncer": 32,
            "nonellipsoidal_int_trend": 45,
            "nonellipsoidal_int_uncertainty": 34,
            "nonellipsoidal_int_plunge": 56,
            "nonellipsoidal_int_plunge_unce": 34,
            "nonellipsoidal_min_value": 23,
            "nonellipsoidal_min_value_uncer": 45,
            "nonellipsoidal_min_trend": 23,
            "nonellipsoidal_min_trend_uncer": 32,
            "nonellipsoidal_min_plunge": 23,
            "nonellipsoidal_min_plunge_unce": 45,
            "non_ellipsoidal_tensor_notes": "Notes here",
            "nonellipsoidal_quality_of_meas": "4",
            "struct_notes": "Tensor notes"
          },
          {
            "type": "other",
            "id": 16529998349655,
            "label": "Other1",
            "feature_type": "boudinage",
            "boudinage_geometry": "unidirectional",
            "boudinage_shape": "symmetrical",
            "boudinage_competent": "Mat",
            "boudinage_incompetent": "Mat",
            "average_width_of_boudin_neck": 34,
            "number_of_necks_measured": 3,
            "boudinage_wavelength_m": 4,
            "boudinaged_layer_thickness_m": 6,
            "boudinage_strike": 23,
            "boudinage_dip_direction": 34,
            "boudinage_dip": 56,
            "boudinage_trend": 23,
            "boudinage_plunge": 43,
            "boudinage_trend_uncertainty": 32,
            "boudinage_2nd_trend": 23,
            "boudinage_2nd_plunge": 34,
            "boudinage_2nd_trend_uncertaint": 12,
            "struct_notes": "Notes"
          },
          {
            "type": "fold",
            "id": 16529996884051,
            "label": "Fold1",
            "feature_type": "monocline",
            "Trend": 23,
            "Plunge": 34,
            "Linearity": "4",
            "Measurement_Quality": "4",
            "Strike": 12,
            "Azimuthal_Dip_Direction": 34,
            "Dip": 32,
            "Planarity": "3",
            "Measurement_Quality_001": "5___excellent",
            "fold_attitude": "vertical",
            "fold_shape": "class_1b__para",
            "tightness": "tight",
            "Hinge_Shape": "subrounded",
            "vergence": "south",
            "wavelength_m": 12,
            "amplitude_m": 23,
            "competent_material_fold": "Mat here",
            "folded_layer_thickness_m": 55,
            "incompetent_material_fold": "Mat here",
            "fold_fol_strike": 12,
            "fold_fol_dip_direction": 23,
            "fold_fol_dip": 34,
            "fold_fol_quality": "approximate",
            "fold_foliation_Type": "axial_planar",
            "fold_foliation_description": "Desc here",
            "fold_notes": "Fold notes here"
          }
        ],
        "fabrics": [
          {
            "type": "fault_rock",
            "id": 16530036019286,
            "label": "Fabric1",
            "inco_nofol": "fault_breccia",
            "inco_nofo_char": "Fab",
            "inco_fol": "foliated_gouge",
            "inco_fo_char": "Fab",
            "co_nofol": "cata",
            "co_nofo_char": "Fab",
            "co_fol": "fol_ultracata",
            "tectonite_type": "s>>l",
            "co_fo_char": "Fab",
            "structural_fabric": [
              "folding",
              "comp_banding"
            ],
            "char_fold": "Fold",
            "comp_band_min": "Zen",
            "spatial_config": [
              "planar",
              "anastomosing"
            ],
            "desc_spat_char": "Desc",
            "kin_ind_present": "yes_kin",
            "kinematic_fab": [
              "oblique_fabric",
              "asymm_fold"
            ],
            "grain_shape_char": "Zrn",
            "asym_fold_char": "Char",
            "sense_of_shear": "Top",
            "interp_note": "Notes"
          },
          {
            "type": "igneous_rock",
            "id": 16530036980941,
            "label": "Fabric2",
            "planar_fab": [
              "no_p_fab",
              "other_p_fab"
            ],
            "lin_fab": [
              "none"
            ],
            "mag_tectonite": "l>s",
            "add_mag_fab": [
              "commingle",
              "mullions"
            ],
            "mag_commingle": "Comm",
            "mag_mullion": "Mull",
            "magmatic_str": [
              "no_mag_str",
              "plume_str"
            ],
            "solid_state_str": [
              "ss_fab",
              "anneal_sz"
            ],
            "char_ss_fab": "Sol",
            "char_ss_sz": "Shear",
            "addition_fab": [
              "structural",
              "other"
            ],
            "str_fab": [
              "folding",
              "fractures"
            ],
            "fold_char": "Fold",
            "fracture_char": "Frac",
            "other_fab_char": "Other",
            "ss_tectonite": "ls",
            "mag_interp_note": "Notes"
          },
          {
            "type": "metamorphic_rock",
            "id": 16530037849501,
            "label": "Fabric3",
            "grain_size": "medium",
            "planar_fabric": [
              "gneissic_band",
              "schistosity"
            ],
            "plan_fab_min_1": "Min",
            "plan_fab_min_2": "Min",
            "plan_fab_min_3": "Min",
            "plan_fab_min_4": "Min",
            "spatial_var": "domainal",
            "length_scale": "Scale",
            "linear_fab": [
              "min_align_lin",
              "intersect_lin"
            ],
            "int_lin_char": "Planes",
            "other_met_fab": [
              "metasom",
              "migmatite"
            ],
            "metasomatic": "Min",
            "migmatitic": "Min",
            "additional_fab": [
              "structural",
              "relict_sed"
            ],
            "structural_fab": [
              "folding",
              "fault"
            ],
            "char_folding": "Char",
            "char_fault": "Char",
            "relict_sed_fab": [
              "bed",
              "flow_top_brecc"
            ],
            "kinematic_ind": "kin_yes",
            "kinematic_fab": [
              "asymm_fold",
              "bookshelf_slip",
              "sigmoidal_gash"
            ],
            "asym_fold_char": "Char",
            "book_slip_char": "Char",
            "sig_gash_char": "Char",
            "sense_of_shear": "Sense here",
            "tectonite_type": "ls",
            "p_t_d_history": "Hist here",
            "interp_note_meta": "Notes"
          }
        ],
        "sed": {
          "strat_section": {
            "strat_section_id": 16530017020988,
            "column_profile": "clastic",
            "column_y_axis_units": "m",
            "section_well_name": "Sec name here",
            "misc_labels": true,
            "display_lithology_patterns": true,
            "section_type": "core",
            "what_core_repository": "Repo here",
            "type_of_corer": "Corer type here",
            "depth_from_surface_to_start_of": "3",
            "total_core_length": "123",
            "location_locality": "Some locality here",
            "basin": "Some basin here",
            "age": "12345",
            "purpose": [
              "geochronology",
              "sequence_strat",
              "pleasure"
            ],
            "project_description": "Desc",
            "dates_of_work": "Dates here",
            "scale_of_interest": [
              "single_basin",
              "single_outcrop",
              "multi_basins",
              "single_core"
            ],
            "obs_interval_bed_obs_scale": "dm",
            "how_is_section_georeferenced": "point_at_secti",
            "strat_section_notes": "Some notes here"
          },
          "character": "package_succe",
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "mudstone",
              "mud_silt_grain_size": "clay",
              "relative_resistance_weather": "1",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "color_appearance": [
                "uniform",
                "patchy",
                "striped"
              ],
              "notes": "Notes here",
              "sand_grain_size": "sand_fine_low",
              "grain_size_range": [
                "sand_fine_low",
                "pebble",
                "pebble",
                "sand_medium_l"
              ],
              "congl_grain_size": "pebble",
              "breccia_grain_size": "pebble",
              "sand_fine_lower_percent": 12,
              "sand_medium_lower_percent": 23,
              "pebble_percent": 34,
              "maximum_clast_size_cm": 12,
              "minimum_clast_size_cm": 23,
              "average_clast_size_cm": 34,
              "matrix_size": [
                "silt",
                "none"
              ],
              "character": [
                "matrix-support",
                "imbrication"
              ],
              "sorting": [
                "well_sorted",
                "mod_sorted"
              ],
              "rounding": [
                "rounded",
                "very_angular"
              ],
              "shape": [
                "spherical",
                "equant"
              ],
              "minerals_present": [
                "quartz",
                "halite",
                "calcite",
                "chert",
                "rip_up_clasts"
              ],
              "sandstone_type_dott": [
                "quartz_arenite",
                "arkosic_arenit"
              ],
              "sandstone_type_folk_mcbride": [
                "quartzarenite",
                "subarkose",
                "sublitharenite"
              ],
              "sandstone_modifier": [
                "rip_up_clasts",
                "wood"
              ],
              "skeletal_carbonate_components": [
                "mollusc",
                "calcareous_alg",
                "brachiopod"
              ],
              "mollusc_percent": 12,
              "brachiopod_percent": 23,
              "calcareous_algae_percent": 34,
              "non_skeletal_carbonate_compone": [
                "mud",
                "oncoid",
                "pisoid"
              ],
              "mud_percent": 12,
              "oncoid_percent": 23,
              "pisoid_percent": 34,
              "clay_or_mudstone_type": [
                "red_mudstone",
                "siliceous_calc"
              ],
              "siliceous_calcareous_mudstone_percent": 12,
              "red_mudstone_percent": 23,
              "conglomerate_composition": [
                "extraformation",
                "monomictic"
              ],
              "clast_composition": [
                "igneous_clast",
                "conglomerate",
                "schist"
              ],
              "conglomerate_clast_percent": 12,
              "matrix_composition": [
                "conglomerate",
                "extrusive_igneous"
              ],
              "extrusive_igneous_matrix_percent": 23,
              "conglomerate_matrix_percent": 34,
              "volcaniclastic_type": [
                "glass"
              ],
              "glass_percent": 12,
              "evaporite_type": [
                "gyp_anhyd_dia"
              ],
              "gypsum_anhydrite_diagenetic_percent": 12,
              "gypsum_anhydrite_diagenetic_type": [
                "nodular_to_chi",
                "displacive"
              ],
              "phosphorite_type": [
                "nodular"
              ],
              "organic_coal_lithologies": [
                "peat",
                "coal_ball"
              ],
              "peat_percent": 12,
              "coal_ball_percent": 23
            }
          ],
          "bedding": {
            "thickness_of_individual_beds": 12,
            "package_bedding_trends": "uniform",
            "beds": [
              {
                "package_geometry": [
                  "discontinuous",
                  "tabular_parall"
                ],
                "shape_of_lower_contacts": [
                  "flat",
                  "irregular"
                ],
                "character_of_lower_contacts": [
                  "flat",
                  "undulatory"
                ],
                "shape_of_upper_contacts": [
                  "undulatory",
                  "curved"
                ],
                "character_of_upper_contacts": [
                  "sharp",
                  "gradational"
                ],
                "upper_contact_relief": "Relief here",
                "notes": "Notes here"
              }
            ]
          },
          "structures": [
            {
              "massive_structureless": "yes",
              "cross_bedding_type": [
                "cross_bedding",
                "trough"
              ],
              "cross_bedding_height_cm": 12,
              "cross_bedding_width_cm": 23,
              "cross_bedding_thickness_cm": 34,
              "cross_bedding_spacing_cm": 45,
              "ripple_lamination_type": [
                "cross_lamin",
                "lenticular"
              ],
              "ripple_lamination_height_mm": 12,
              "ripple_lamination_width_mm": 23,
              "ripple_lamination_thick_mm": 23,
              "ripple_lamination_spacing_mm": 34,
              "horizontal_bedding_type": [
                "horizontal",
                "planar"
              ],
              "graded_bedding_type": "normally_grade",
              "deformation_structures": [
                "contorted_bedd",
                "dikes"
              ],
              "lag_type": [
                "lag_deposit",
                "rip_up_clasts"
              ],
              "clast_composition": "Comp",
              "clast_size": "12",
              "layer_thickness_shape": "23",
              "other_common_structures": [
                "bouma_sequence"
              ],
              "bouma_sequence_part": [
                "a"
              ],
              "notes": "Notes here",
              "bioturbation_index": "1_sparse",
              "bedding_plane_features": [
                "bedforms",
                "gutter_cast"
              ],
              "bedding_plane_features_scale": "12",
              "bedform_type": [
                "wave_ripples",
                "3d_crests",
                "ladderback"
              ],
              "bedding_plane_features_orientation": "12",
              "bedform_scale": "23",
              "crest_orientation_azimuth_0_360": "45",
              "paleosol_horizons": [
                "o",
                "c"
              ],
              "o_horizon_thickness_cm": 12,
              "c_horizon_thickness_cm": 23,
              "paleosol_structures": [
                "peds",
                "leaching_horiz"
              ],
              "additional_modifiers": "Additional here",
              "paleosol_classification": [
                "gelisol",
                "histosol"
              ]
            }
          ],
          "diagenesis": [
            {
              "cement_composition": [
                "calcite",
                "clay"
              ],
              "vein_type": "parallel",
              "vein_width": 12,
              "vein_length": 23,
              "vein_orientation": "45",
              "vein_mineralogy": "iron_oxides",
              "fracture_type": "oblique",
              "fracture_width": 12,
              "fracture_length": 23,
              "fracture_orientation": "Or",
              "fracture_mineralogy": "evaporite_min",
              "nodules_concretions_size": "mm",
              "min": 12,
              "max": 45,
              "average": 55,
              "nodules_concretions_shape": [
                "spherical",
                "irregular"
              ],
              "spacing": 33,
              "nodules_concretions_type": "layered",
              "nodules_concretions_comp": [
                "calcite",
                "gypsum_anhydri"
              ],
              "replacement_type": "fossil_selecti",
              "recrystallization_type": "local",
              "other_diagenetic_features": [
                "stylolites",
                "liesegang_band"
              ],
              "fabric_selective": [
                "interparticle",
                "intraparticle"
              ],
              "non_selective": [
                "channel",
                "vug"
              ],
              "carbonate_desicc_and_diss": [
                "grykes",
                "sheet_cracks"
              ],
              "notes": "Notes here"
            }
          ],
          "fossils": [
            {
              "invertebrate": [
                "porifera_spong",
                "cnidaria",
                "chordata",
                "mollusca"
              ],
              "mollusca": [
                "cephalopod",
                "belemnite"
              ],
              "chordate": "tunicate",
              "plant_algae": [
                "red_algae",
                "phylloid"
              ],
              "vertebrate": [
                "chondrichthyes",
                "aves"
              ],
              "faunal_assemblage": "heterozoan",
              "diversity": "medium",
              "descriptive": [
                "track",
                "sub_vertical"
              ],
              "burrow_fill_type": [
                "mudstone",
                "active"
              ],
              "behavioral_grouping": [
                "locomotion",
                "farming"
              ],
              "ichnofacies": "skolithos",
              "list_of_specific_types": "Types here",
              "dominant_component": "microbial_reef",
              "other_dominant_component": "Other dom here",
              "microbial_reef_or_skelatal_mic": [
                "micro_laminate",
                "tufa"
              ],
              "other_microbial_or_skeletal_mi": "Other mic here",
              "height": "12",
              "width": "23",
              "orientation_if_elongate_azimu": 45,
              "shape": "dome",
              "type": "fringing",
              "accessory_structures": [
                "fenestrae",
                "geopetal"
              ],
              "notes": "Notes here"
            }
          ],
          "interpretations": [
            {
              "sediment_transport": [
                "waves",
                "turbidity_curr"
              ],
              "fluidization": "liquefaction",
              "miscellaneous": [
                "ice_rafting",
                "desiccation"
              ],
              "notes": "Notes here",
              "general": [
                "continental",
                "transitional"
              ],
              "clastic": [
                "playa",
                "glacial_and_pr"
              ],
              "glacial_and_proglacial_environ": [
                "till",
                "outwash"
              ],
              "carbonates": [
                "factory"
              ],
              "factory": [
                "photozoan",
                "metozoan"
              ],
              "geometry": "undulatory",
              "relief_scale": "cm",
              "extent": "23",
              "extent_scale": "m",
              "relief": "12",
              "type": [
                "mineralization",
                "pedogenic"
              ],
              "stratal_termination": "toplap",
              "general_surfaces": "Gen surf",
              "sequence_stratigraphic_surfaces": "type_3_sequenc",
              "named": "Named here",
              "description": [
                "fining_upward",
                "isolated"
              ],
              "stacking_sequence_stratigraphy": [
                "progradational",
                "highstand_syst"
              ],
              "fluvial_architectural_elements": [
                "gravelly_bar_o",
                "sandy_bedform"
              ],
              "lacustrine_architecture_interpretation": [
                "overfilled",
                "balanced"
              ],
              "carbonate_platform_geometry": [
                "attached",
                "unrimmed_platf"
              ],
              "deep_water_architctural_element": [
                "levee",
                "sheet"
              ],
              "carbonate_margin_geometry": [
                "accretionary_m",
                "other"
              ],
              "other_carbonate_margin_geometry": "Other geometry"
            }
          ]
        },
        "samples": [
          {
            "sample_type": "field",
            "id": 16530015451321,
            "sample_id_name": "Efg345",
            "label": "Sample1",
            "main_sampling_purpose": "geochronology",
            "deposit_thickness": "23",
            "sample_description": "Samp desc here",
            "material_type": "sediment",
            "inplaceness_of_sample": "5___definitely",
            "oriented_sample": "yes",
            "sample_orientation_notes": "Notes here",
            "sample_size": "123",
            "degree_of_weathering": "4",
            "sample_notes": "Some notes"
          }
        ],
        "gps_accuracy": 1.23,
        "name": "Spot1",
        "time": "2022-06-19T22:27:11.000Z",
        "id": 16529992313378,
        "pet": {
          "volcanic_rock_type": [
            "latite"
          ],
          "igneous_rock_class": [
            "volcanic"
          ],
          "rock_type": [
            "igneous"
          ],
          "occurence_volcanic": [
            "dome",
            "unclear"
          ],
          "texture_volcanic": [
            "clastic",
            "aphanitic"
          ],
          "color_index_volc": 23,
          "color_index_source_volc": "strabotools",
          "vol_characteristic_size_of_cry": 123,
          "structure_volcanic": [
            "eutaxitic"
          ],
          "alteration_volcanic": [
            "metamorphic_ov"
          ],
          "notes_volcanic": "Notes here",
          "minerals": [
            {
              "id": 16530034561873,
              "full_mineral_name": "Zircon",
              "mineral_abbrev": "zrn",
              "habit": "acicular",
              "textural_setting_igneous": [
                "phenocryst",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 12,
              "maximum_grain_size_mm": 23,
              "modal": 34,
              "mineral_notes": "Mineral notes here"
            },
            {
              "id": 16530035059185,
              "full_mineral_name": "Aegirine",
              "mineral_abbrev": "aeg",
              "habit": "euhedral",
              "textural_setting_igneous": [
                "vesicle",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 1,
              "maximum_grain_size_mm": 2,
              "modal": 3,
              "mineral_notes": "Notes here"
            }
          ],
          "reactions": [
            {
              "id": 16530035338583,
              "reactions": "Ab=zn+bc",
              "based_on": [
                "corona",
                "mineral_degrad"
              ],
              "notes": "Notes here"
            }
          ]
        },
        "spot_radius": 1.3,
        "self": "https://strabospot.org/db/feature/16529992313378"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -97.679878,
          38.576911
        ]
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0,
              0
            ],
            [
              0,
              80
            ],
            [
              20,
              80
            ],
            [
              20,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-05-19T23:11:15.000Z",
        "altitude": 405.94,
        "lng": -97.679578,
        "strat_section_id": 16530017020988,
        "surface_feature": {
          "surface_feature_type": "strat_interval"
        },
        "modified_timestamp": 1653001875459,
        "sed": {
          "character": "bed",
          "interval": {
            "interval_thickness": 4,
            "thickness_units": "m"
          },
          "bedding": {
            "beds": [
              {
                "notes": "Notes here"
              }
            ]
          },
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "siltstone",
              "mud_silt_grain_size": "silt",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "relative_resistance_weather": "3",
              "notes": "Notes here"
            }
          ]
        },
        "name": "Abc123",
        "time": "2022-05-19T23:11:15.000Z",
        "id": 16530018754410,
        "lat": 38.577,
        "self": "https://strabospot.org/db/feature/16530018754410"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Point",
        "coordinates": [
          2705.0625,
          1775.8125
        ]
      },
      "properties": {
        "date": "2022-08-10T16:29:43.000Z",
        "lng": -97.679878,
        "image_basemap": 16530015128805,
        "name": "On image",
        "time": "2022-08-10T16:29:43.000Z",
        "id": 16601489837307,
        "lat": 38.576911,
        "modified_timestamp": 1660148995221,
        "self": "https://strabospot.org/db/feature/16601489837307"
      },
      "type": "Feature"
    }
  ]
},
{
  "type": "FeatureCollection",
  "features": [
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-97.676182, 38.578769],
            [-97.674251, 38.579943],
            [-97.673500, 38.578198],
            [-97.676182, 38.578769]
          ]
        ]
      },
      "properties": {
        "date": "2022-08-12T10:15:20.000Z",
        "name": "Abc226",
        "time": "2022-08-12T10:15:20.000Z",
        "id": 17601490430653,
        "modified_timestamp": 1660299320000,
        "self": "https://strabospot.org/db/feature/17601490430653"
      },
      "type": "Feature"
    },

    {
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [-97.679658, 38.578886],
          [-97.674508, 38.576907],
          [-97.671762, 38.578484]
        ]
      },
      "properties": {
        "date": "2022-08-12T10:14:10.000Z",
        "name": "Abc225",
        "time": "2022-08-12T10:14:10.000Z",
        "id": 17601490340852,
        "modified_timestamp": 1660299250000,
        "self": "https://strabospot.org/db/feature/17601490340852"
      },
      "type": "Feature"
    },

    {
      "properties": {
        "images": [
          {
            "width": 4096,
            "caption": "Alternate field view",
            "id": 17530015128806,
            "title": "My image 2",
            "annotated": false,
            "height": 3072,
            "image_type": "photo",
            "self": "https://strabospot.org/db/image/17530015128806"
          }
        ],
        "date": "2022-06-21T15:05:45.000Z",
        "altitude": 24,
        "notes": "Second spot: fresh fracture surface and subtle imbrication.",
        "data": {
          "urls": [
            "https://macrostrat.org",
            "http://example.com/resource"
          ]
        },
        "other_features": [
          {
            "id": 17530016041795,
            "label": "OthFeat-2",
            "type": "hydrologic",
            "name": "Small spring",
            "description": "Seep along contact"
          }
        ],
        "orientation_data": [
          {
            "type": "planar_orientation",
            "id": 17529994975257,
            "label": "Plane2",
            "strike": 135,
            "dip_direction": 225,
            "dip": 32,
            "quality": "3",
            "feature_type": "fracture",
            "fracture_type": "opening_mode",
            "fracture_defined_by": "trace",
            "movement": "nw_side_up",
            "movement_justification": ["not_specified"],
            "directional_indicators": ["slickenfibers"],
            "thickness": 1.5,
            "length": 2.2,
            "notes": "Clean surface"
          },
          {
            "type": "linear_orientation",
            "id": 17529995763665,
            "label": "LineA",
            "trend": 20,
            "plunge": 18,
            "rake": 25,
            "rake_calculated": "no",
            "quality": "3",
            "feature_type": "z_fold",
            "defined_by": "hinge",
            "notes": "Subtle"
          },
          {
            "type": "tabular_orientation",
            "id": 17529996088030,
            "label": "Tab zone 2",
            "strike": 30,
            "dip_direction": 60,
            "dip": 50,
            "quality": "3",
            "feature_type": "vein",
            "vein_type": "normal_opening",
            "vein_fill": "calcite",
            "thickness": 18,
            "tabularity": "semi_constant",
            "length": 21,
            "defined_by": "continuous",
            "notes": "Calcite-filled"
          }
        ],
        "modified_timestamp": 1660332345000,
        "_3d_structures": [
          {
            "type": "fabric",
            "id": 17529996735747,
            "feature_type": "tectonite",
            "tectonite_type": "sl_tectonite",
            "tectonite_character": "s___l",
            "struct_notes": "Weak S>>L overprint",
            "label": "tectonite-2"
          },
          {
            "type": "tensor",
            "id": 17529997746294,
            "label": "Tensor2",
            "feature_type": "non_ellipsoidal_data",
            "non_ellipsoidal_type": "flow_apophyses",
            "nonellipsoidal_max_value": 25,
            "nonellipsoidal_max_value_uncer": 40,
            "nonellipsoidal_max_trend": 60,
            "nonellipsoidal_max_trend_uncer": 30,
            "nonellipsoidal_max_plunge": 20,
            "nonellipsoidal_max_plunge_unce": 45,
            "nonellipsoidal_int_value": 22,
            "nonellipsoidal_int_value_uncer": 30,
            "nonellipsoidal_int_trend": 42,
            "nonellipsoidal_int_uncertainty": 28,
            "nonellipsoidal_int_plunge": 50,
            "nonellipsoidal_int_plunge_unce": 33,
            "nonellipsoidal_min_value": 18,
            "nonellipsoidal_min_value_uncer": 38,
            "nonellipsoidal_min_trend": 28,
            "nonellipsoidal_min_trend_uncer": 26,
            "nonellipsoidal_min_plunge": 18,
            "nonellipsoidal_min_plunge_unce": 40,
            "non_ellipsoidal_tensor_notes": "Comparable to nearby station",
            "nonellipsoidal_quality_of_meas": "3",
            "struct_notes": "Notes updated"
          }
        ],
        "fabrics": [
          {
            "type": "fault_rock",
            "id": 17530036019286,
            "label": "FabricA",
            "inco_nofol": "fault_breccia",
            "inco_nofo_char": "Angular fragments",
            "inco_fol": "foliated_gouge",
            "inco_fo_char": "Sheared clay",
            "co_nofol": "cata",
            "co_nofo_char": "Milled grains",
            "co_fol": "fol_ultracata",
            "tectonite_type": "s>>l",
            "co_fo_char": "Ultracataclasite bands",
            "structural_fabric": ["folding", "comp_banding"],
            "char_fold": "Open",
            "comp_band_min": "Qz",
            "spatial_config": ["planar", "anastomosing"],
            "desc_spat_char": "Interconnected bands",
            "kin_ind_present": "yes_kin",
            "kinematic_fab": ["oblique_fabric"],
            "grain_shape_char": "Subangular",
            "asym_fold_char": "Weak",
            "sense_of_shear": "Top-to-SE",
            "interp_note": "Localized"
          }
        ],
        "sed": {
          "strat_section": {
            "strat_section_id": 17530017020988,
            "column_profile": "clastic",
            "column_y_axis_units": "m",
            "section_well_name": "Sec name here",
            "misc_labels": true,
            "display_lithology_patterns": true,
            "section_type": "core",
            "what_core_repository": "Repo here",
            "type_of_corer": "Wireline",
            "depth_from_surface_to_start_of": "4",
            "total_core_length": "118",
            "location_locality": "Locality B",
            "basin": "Another basin",
            "age": "12346",
            "purpose": ["geochronology", "sequence_strat"],
            "project_description": "Desc 2",
            "dates_of_work": "Dates 2",
            "scale_of_interest": ["single_outcrop", "single_core"],
            "obs_interval_bed_obs_scale": "dm",
            "how_is_section_georeferenced": "point_at_secti",
            "strat_section_notes": "Alt notes"
          },
          "character": "package_succe",
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "mudstone",
              "mud_silt_grain_size": "clay",
              "relative_resistance_weather": "2",
              "lithification": "poorly_lithifi",
              "fresh_color": "Brown",
              "weathered_color": "Light brown",
              "color_appearance": ["uniform", "striped"],
              "notes": "Variably bioturbated",
              "sand_grain_size": "sand_fine_low",
              "grain_size_range": ["sand_fine_low", "sand_medium_l"],
              "congl_grain_size": "pebble",
              "breccia_grain_size": "pebble",
              "sand_fine_lower_percent": 10,
              "sand_medium_lower_percent": 20,
              "pebble_percent": 25,
              "maximum_clast_size_cm": 10,
              "minimum_clast_size_cm": 20,
              "average_clast_size_cm": 28,
              "matrix_size": ["silt"],
              "character": ["matrix-support"],
              "sorting": ["mod_sorted"],
              "rounding": ["rounded", "subangular"],
              "shape": ["equant"],
              "minerals_present": ["quartz", "calcite", "chert"],
              "sandstone_type_dott": ["quartz_arenite"],
              "sandstone_type_folk_mcbride": ["quartzarenite"],
              "sandstone_modifier": ["wood"],
              "skeletal_carbonate_components": ["mollusc"],
              "mollusc_percent": 8,
              "non_skeletal_carbonate_compone": ["mud"],
              "mud_percent": 15
            }
          ]
        },
        "samples": [
          {
            "sample_type": "field",
            "id": 17530015451321,
            "sample_id_name": "Hij678",
            "label": "Sample2",
            "main_sampling_purpose": "geochronology",
            "deposit_thickness": "18",
            "sample_description": "Fine mudstone with plant debris",
            "material_type": "sediment",
            "inplaceness_of_sample": "4___probable",
            "oriented_sample": "no",
            "sample_orientation_notes": "NA",
            "sample_size": "110",
            "degree_of_weathering": "3",
            "sample_notes": "Collected from fresh surface"
          }
        ],
        "gps_accuracy": 2.5,
        "name": "Spot2",
        "time": "2022-06-21T15:05:45.000Z",
        "id": 17529992313379,
        "pet": {
          "volcanic_rock_type": ["trachyte"],
          "igneous_rock_class": ["volcanic"],
          "rock_type": ["igneous"],
          "occurence_volcanic": ["flow", "unclear"],
          "texture_volcanic": ["aphanitic"],
          "color_index_volc": 18,
          "color_index_source_volc": "strabotools",
          "vol_characteristic_size_of_cry": 95,
          "structure_volcanic": ["eutaxitic"],
          "alteration_volcanic": ["propylitic"],
          "notes_volcanic": "Weak alteration halos",
          "minerals": [
            {
              "id": 17530034561873,
              "full_mineral_name": "Zircon",
              "mineral_abbrev": "zrn",
              "habit": "prismatic",
              "textural_setting_igneous": ["phenocryst"],
              "textural_setting_metamorphic": ["lineation_defi"],
              "average_grain_size_mm": 0.8,
              "maximum_grain_size_mm": 1.6,
              "modal": 2,
              "mineral_notes": "Sparse"
            }
          ],
          "reactions": [
            {
              "id": 17530035338583,
              "reactions": "Ab = An + Qtz",
              "based_on": ["textures"],
              "notes": "Tentative"
            }
          ]
        },
        "spot_radius": 1.6,
        "self": "https://strabospot.org/db/feature/17529992313379"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-97.679520, 38.577220]
      },
      "type": "Feature"
    },

    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [0, 0],
            [0, 80],
            [20, 80],
            [20, 0],
            [0, 0]
          ]
        ]
      },
      "properties": {
        "date": "2022-05-21T12:00:00.000Z",
        "altitude": 406.25,
        "lng": -97.679400,
        "strat_section_id": 17530017020988,
        "surface_feature": {
          "surface_feature_type": "strat_interval"
        },
        "modified_timestamp": 1653134400000,
        "sed": {
          "character": "bed",
          "interval": {
            "interval_thickness": 3.5,
            "thickness_units": "m"
          },
          "bedding": {
            "beds": [
              {
                "notes": "Subtle gradation upward"
              }
            ]
          },
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "siltstone",
              "mud_silt_grain_size": "silt",
              "lithification": "poorly_lithifi",
              "fresh_color": "Gray",
              "weathered_color": "Tan",
              "relative_resistance_weather": "3",
              "notes": "Ripple lamination present"
            }
          ]
        },
        "name": "Abc223",
        "time": "2022-05-21T12:00:00.000Z",
        "id": 17530018754411,
        "lat": 38.577200,
        "self": "https://strabospot.org/db/feature/17530018754411"
      },
      "type": "Feature"
    },

    {
      "geometry": {
        "type": "Point",
        "coordinates": [2705.0625, 1775.8125]
      },
      "properties": {
        "date": "2022-08-12T10:13:05.000Z",
        "lng": -97.679878,
        "image_basemap": 17530015128806,
        "name": "On image 2",
        "time": "2022-08-12T10:13:05.000Z",
        "id": 17601489837308,
        "lat": 38.576911,
        "modified_timestamp": 1660299185000,
        "self": "https://strabospot.org/db/feature/17601489837308"
      },
      "type": "Feature"
    }
  ]
}]
```
</details>

**Response** — `200 OK`
<details>
<summary>Example response body ([FieldSite, ...])</summary>

```json
[
    {
        "id": 16529992313378,
        "name": null,
        "location": {
            "latitude": 38.576911,
            "longitude": -97.679878,
            "elevation": null,
            "radius": null,
            "description": null,
            "closest_place": null,
            "gps_accuracy": null
        },
        "created": "2022-06-19T22:27:11Z",
        "updated": "2022-08-10T16:29:39.966000Z",
        "observations": [
            {
                "notes": null,
                "data": {
                    "strike": 123.0,
                    "dip": 45.0,
                    "facing": "upright",
                    "notes": null,
                    "associated": []
                }
            }
        ],
        "samples": [],
        "photos": [
            {
                "id": 16530015128805,
                "url": "rockd://photo/16530015128805",
                "width": 4032,
                "height": 3024,
                "checksum": ""
            }
        ],
        "notes": "Spot notes here",
        "social": null,
        "children": null,
        "contributors": null
    },
    {
        "id": 17529992313379,
        "name": null,
        "location": {
            "latitude": 38.57722,
            "longitude": -97.67952,
            "elevation": null,
            "radius": null,
            "description": null,
            "closest_place": null,
            "gps_accuracy": null
        },
        "created": "2022-06-21T15:05:45Z",
        "updated": "2022-08-12T19:25:45Z",
        "observations": [
            {
                "notes": null,
                "data": {
                    "strike": 135.0,
                    "dip": 32.0,
                    "facing": "upright",
                    "notes": null,
                    "associated": []
                }
            }
        ],
        "samples": [],
        "photos": [
            {
                "id": 17530015128806,
                "url": "rockd://photo/17530015128806",
                "width": 4096,
                "height": 3072,
                "checksum": ""
            }
        ],
        "notes": "Second spot: fresh fracture surface and subtle imbrication.",
        "social": null,
        "children": null,
        "contributors": null
    }
]
```
</details>

---

## POST `/interchange-data/fieldsite-to-checkin`

Converts **FieldSite(s)** → Rockd **checkin** payload(s).  
> This endpoint expects an **array**; to send a single FieldSite, pass an array of length 1.

### Single (array-of-one)
<details>
<summary>Request body ([FieldSite])</summary>

```json
[
    {
        "id": 16529992313378,
        "name": null,
        "location": {
            "latitude": 38.576911,
            "longitude": -97.679878,
            "elevation": null,
            "radius": null,
            "description": null,
            "closest_place": null,
            "gps_accuracy": null
        },
        "created": "2022-06-19T22:27:11Z",
        "updated": "2022-08-10T16:29:39.966000Z",
        "observations": [
            {
                "notes": null,
                "data": {
                    "strike": 123.0,
                    "dip": 45.0,
                    "facing": "upright",
                    "notes": null,
                    "associated": []
                }
            }
        ],
        "samples": [],
        "photos": [
            {
                "id": 16530015128805,
                "url": "rockd://photo/16530015128805",
                "width": 4032,
                "height": 3024,
                "checksum": ""
            }
        ],
        "notes": "Spot notes here",
        "social": null,
        "children": null,
        "contributors": null
    }
]
```
</details>

### Multiple
<details>
<summary>Request body ([FieldSite, ...])</summary>

```json
[
    {
        "id": 16529992313378,
        "name": null,
        "location": {
            "latitude": 38.576911,
            "longitude": -97.679878,
            "elevation": null,
            "radius": null,
            "description": null,
            "closest_place": null,
            "gps_accuracy": null
        },
        "created": "2022-06-19T22:27:11Z",
        "updated": "2022-08-10T16:29:39.966000Z",
        "observations": [
            {
                "notes": null,
                "data": {
                    "strike": 123.0,
                    "dip": 45.0,
                    "facing": "upright",
                    "notes": null,
                    "associated": []
                }
            }
        ],
        "samples": [],
        "photos": [
            {
                "id": 16530015128805,
                "url": "rockd://photo/16530015128805",
                "width": 4032,
                "height": 3024,
                "checksum": ""
            }
        ],
        "notes": "Spot notes here",
        "social": null,
        "children": null,
        "contributors": null
    },
    {
        "id": 17529992313379,
        "name": null,
        "location": {
            "latitude": 38.57722,
            "longitude": -97.67952,
            "elevation": null,
            "radius": null,
            "description": null,
            "closest_place": null,
            "gps_accuracy": null
        },
        "created": "2022-06-21T15:05:45Z",
        "updated": "2022-08-12T19:25:45Z",
        "observations": [
            {
                "notes": null,
                "data": {
                    "strike": 135.0,
                    "dip": 32.0,
                    "facing": "upright",
                    "notes": null,
                    "associated": []
                }
            }
        ],
        "samples": [],
        "photos": [
            {
                "id": 17530015128806,
                "url": "rockd://photo/17530015128806",
                "width": 4096,
                "height": 3072,
                "checksum": ""
            }
        ],
        "notes": "Second spot: fresh fracture surface and subtle imbrication.",
        "social": null,
        "children": null,
        "contributors": null
    }
]
```
</details>

**Response** — `200 OK`
<details>
<summary>Example response body ([checkin, ...])</summary>

```json
[
    {
        "checkin_id": 16529992313378,
        "notes": "Spot notes here",
        "lat": 38.576911,
        "lng": -97.679878,
        "created": "2022-06-19T22:27:11+00:00",
        "photo": 16530015128805,
        "observations": [
            {
                "orientation": {
                    "strike": 123.0,
                    "dip": 45.0
                }
            }
        ]
    },
    {
        "checkin_id": 17529992313379,
        "notes": "Second spot: fresh fracture surface and subtle imbrication.",
        "lat": 38.57722,
        "lng": -97.67952,
        "created": "2022-06-21T15:05:45+00:00",
        "photo": 17530015128806,
        "observations": [
            {
                "orientation": {
                    "strike": 135.0,
                    "dip": 32.0
                }
            }
        ]
    }
]
```
</details>

---

## POST `/interchange-data/spot-to-checkin`

Pipeline: **Spot FeatureCollection(s)** → **checkin(s)**. FieldSite conversion is behind the scenes.

This route accepts **two** input shapes:
1) Single Spot/FeatureCollection, 2) Array of Spots/FeatureCollections

### (1) Single FeatureCollection
<details>
<summary>Request body (FeatureCollection)</summary>

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -97.676182,
              38.578769
            ],
            [
              -97.674251,
              38.579943
            ],
            [
              -97.6735,
              38.578198
            ],
            [
              -97.676182,
              38.578769
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:43.000Z",
        "name": "Abc126",
        "time": "2022-08-10T16:30:43.000Z",
        "id": 16601490430653,
        "modified_timestamp": 1660149043065,
        "self": "https://strabospot.org/db/feature/16601490430653"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            -97.679658,
            38.578886
          ],
          [
            -97.674508,
            38.576907
          ],
          [
            -97.671762,
            38.578484
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:34.000Z",
        "name": "Abc125",
        "time": "2022-08-10T16:30:34.000Z",
        "id": 16601490340852,
        "modified_timestamp": 1660149034086,
        "self": "https://strabospot.org/db/feature/16601490340852"
      },
      "type": "Feature"
    },
    {
      "properties": {
        "images": [
          {
            "width": 4032,
            "caption": "Image description here",
            "id": 16530015128805,
            "title": "My image",
            "annotated": true,
            "height": 3024,
            "image_type": "photo",
            "self": "https://strabospot.org/db/image/16530015128805"
          }
        ],
        "date": "2022-06-19T22:27:11.000Z",
        "altitude": 23,
        "notes": "Spot notes here",
        "data": {
          "urls": [
            "http://www.google.com"
          ]
        },
        "other_features": [
          {
            "id": 16530016041795,
            "label": "OthFeat",
            "type": "hydrologic",
            "name": "Feature Name",
            "description": "Desc here"
          }
        ],
        "orientation_data": [
          {
            "type": "planar_orientation",
            "id": 16529994975257,
            "label": "Plane1",
            "strike": 123,
            "dip_direction": 234,
            "dip": 45,
            "quality": "4",
            "feature_type": "fracture",
            "fracture_type": "opening_mode",
            "fracture_defined_by": "Something",
            "movement": "se_side_up",
            "movement_justification": [
              "not_specified",
              "offset_foliation"
            ],
            "directional_indicators": [
              "riedel_shear",
              "slickenfibers"
            ],
            "thickness": 2,
            "length": 3,
            "notes": "Pl feat notes"
          },
          {
            "type": "linear_orientation",
            "id": 16529995763665,
            "label": "Line1",
            "trend": 12,
            "plunge": 23,
            "rake": 34,
            "rake_calculated": "no",
            "quality": "3",
            "feature_type": "z_fold",
            "defined_by": "Something",
            "notes": "Notes here"
          },
          {
            "type": "tabular_orientation",
            "id": 16529996088030,
            "label": "Tab zone 1",
            "strike": 23,
            "dip_direction": 45,
            "dip": 55,
            "quality": "3",
            "feature_type": "vein",
            "vein_type": "normal_opening",
            "vein_fill": "quartz",
            "thickness": 23,
            "tabularity": "semi_constant",
            "length": 23,
            "defined_by": "Something here",
            "notes": "Tab notes"
          },
          {
            "type": "linear_orientation",
            "id": 16590144068585,
            "label": "Line2",
            "trend": 44,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144221415,
            "label": "line3",
            "trend": 55,
            "plunge": 66,
            "rake": 77,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144415915,
            "label": "line4",
            "trend": 11,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          }
        ],
        "modified_timestamp": 1660148979966,
        "_3d_structures": [
          {
            "type": "fabric",
            "id": 16529996735747,
            "feature_type": "tectonite",
            "tectonite_type": "sl_tectonite",
            "tectonite_character": "s___l",
            "struct_notes": "Fab notes",
            "label": "tectonite"
          },
          {
            "type": "tensor",
            "id": 16529997746294,
            "label": "Tensor1",
            "feature_type": "non_ellipsoidal_data",
            "non_ellipsoidal_type": "flow_apophyses",
            "nonellipsoidal_max_value": 23,
            "nonellipsoidal_max_value_uncer": 43,
            "nonellipsoidal_max_trend": 56,
            "nonellipsoidal_max_trend_uncer": 34,
            "nonellipsoidal_max_plunge": 23,
            "nonellipsoidal_max_plunge_unce": 54,
            "nonellipsoidal_int_value": 23,
            "nonellipsoidal_int_value_uncer": 32,
            "nonellipsoidal_int_trend": 45,
            "nonellipsoidal_int_uncertainty": 34,
            "nonellipsoidal_int_plunge": 56,
            "nonellipsoidal_int_plunge_unce": 34,
            "nonellipsoidal_min_value": 23,
            "nonellipsoidal_min_value_uncer": 45,
            "nonellipsoidal_min_trend": 23,
            "nonellipsoidal_min_trend_uncer": 32,
            "nonellipsoidal_min_plunge": 23,
            "nonellipsoidal_min_plunge_unce": 45,
            "non_ellipsoidal_tensor_notes": "Notes here",
            "nonellipsoidal_quality_of_meas": "4",
            "struct_notes": "Tensor notes"
          },
          {
            "type": "other",
            "id": 16529998349655,
            "label": "Other1",
            "feature_type": "boudinage",
            "boudinage_geometry": "unidirectional",
            "boudinage_shape": "symmetrical",
            "boudinage_competent": "Mat",
            "boudinage_incompetent": "Mat",
            "average_width_of_boudin_neck": 34,
            "number_of_necks_measured": 3,
            "boudinage_wavelength_m": 4,
            "boudinaged_layer_thickness_m": 6,
            "boudinage_strike": 23,
            "boudinage_dip_direction": 34,
            "boudinage_dip": 56,
            "boudinage_trend": 23,
            "boudinage_plunge": 43,
            "boudinage_trend_uncertainty": 32,
            "boudinage_2nd_trend": 23,
            "boudinage_2nd_plunge": 34,
            "boudinage_2nd_trend_uncertaint": 12,
            "struct_notes": "Notes"
          },
          {
            "type": "fold",
            "id": 16529996884051,
            "label": "Fold1",
            "feature_type": "monocline",
            "Trend": 23,
            "Plunge": 34,
            "Linearity": "4",
            "Measurement_Quality": "4",
            "Strike": 12,
            "Azimuthal_Dip_Direction": 34,
            "Dip": 32,
            "Planarity": "3",
            "Measurement_Quality_001": "5___excellent",
            "fold_attitude": "vertical",
            "fold_shape": "class_1b__para",
            "tightness": "tight",
            "Hinge_Shape": "subrounded",
            "vergence": "south",
            "wavelength_m": 12,
            "amplitude_m": 23,
            "competent_material_fold": "Mat here",
            "folded_layer_thickness_m": 55,
            "incompetent_material_fold": "Mat here",
            "fold_fol_strike": 12,
            "fold_fol_dip_direction": 23,
            "fold_fol_dip": 34,
            "fold_fol_quality": "approximate",
            "fold_foliation_Type": "axial_planar",
            "fold_foliation_description": "Desc here",
            "fold_notes": "Fold notes here"
          }
        ],
        "fabrics": [
          {
            "type": "fault_rock",
            "id": 16530036019286,
            "label": "Fabric1",
            "inco_nofol": "fault_breccia",
            "inco_nofo_char": "Fab",
            "inco_fol": "foliated_gouge",
            "inco_fo_char": "Fab",
            "co_nofol": "cata",
            "co_nofo_char": "Fab",
            "co_fol": "fol_ultracata",
            "tectonite_type": "s>>l",
            "co_fo_char": "Fab",
            "structural_fabric": [
              "folding",
              "comp_banding"
            ],
            "char_fold": "Fold",
            "comp_band_min": "Zen",
            "spatial_config": [
              "planar",
              "anastomosing"
            ],
            "desc_spat_char": "Desc",
            "kin_ind_present": "yes_kin",
            "kinematic_fab": [
              "oblique_fabric",
              "asymm_fold"
            ],
            "grain_shape_char": "Zrn",
            "asym_fold_char": "Char",
            "sense_of_shear": "Top",
            "interp_note": "Notes"
          },
          {
            "type": "igneous_rock",
            "id": 16530036980941,
            "label": "Fabric2",
            "planar_fab": [
              "no_p_fab",
              "other_p_fab"
            ],
            "lin_fab": [
              "none"
            ],
            "mag_tectonite": "l>s",
            "add_mag_fab": [
              "commingle",
              "mullions"
            ],
            "mag_commingle": "Comm",
            "mag_mullion": "Mull",
            "magmatic_str": [
              "no_mag_str",
              "plume_str"
            ],
            "solid_state_str": [
              "ss_fab",
              "anneal_sz"
            ],
            "char_ss_fab": "Sol",
            "char_ss_sz": "Shear",
            "addition_fab": [
              "structural",
              "other"
            ],
            "str_fab": [
              "folding",
              "fractures"
            ],
            "fold_char": "Fold",
            "fracture_char": "Frac",
            "other_fab_char": "Other",
            "ss_tectonite": "ls",
            "mag_interp_note": "Notes"
          },
          {
            "type": "metamorphic_rock",
            "id": 16530037849501,
            "label": "Fabric3",
            "grain_size": "medium",
            "planar_fabric": [
              "gneissic_band",
              "schistosity"
            ],
            "plan_fab_min_1": "Min",
            "plan_fab_min_2": "Min",
            "plan_fab_min_3": "Min",
            "plan_fab_min_4": "Min",
            "spatial_var": "domainal",
            "length_scale": "Scale",
            "linear_fab": [
              "min_align_lin",
              "intersect_lin"
            ],
            "int_lin_char": "Planes",
            "other_met_fab": [
              "metasom",
              "migmatite"
            ],
            "metasomatic": "Min",
            "migmatitic": "Min",
            "additional_fab": [
              "structural",
              "relict_sed"
            ],
            "structural_fab": [
              "folding",
              "fault"
            ],
            "char_folding": "Char",
            "char_fault": "Char",
            "relict_sed_fab": [
              "bed",
              "flow_top_brecc"
            ],
            "kinematic_ind": "kin_yes",
            "kinematic_fab": [
              "asymm_fold",
              "bookshelf_slip",
              "sigmoidal_gash"
            ],
            "asym_fold_char": "Char",
            "book_slip_char": "Char",
            "sig_gash_char": "Char",
            "sense_of_shear": "Sense here",
            "tectonite_type": "ls",
            "p_t_d_history": "Hist here",
            "interp_note_meta": "Notes"
          }
        ],
        "sed": {
          "strat_section": {
            "strat_section_id": 16530017020988,
            "column_profile": "clastic",
            "column_y_axis_units": "m",
            "section_well_name": "Sec name here",
            "misc_labels": true,
            "display_lithology_patterns": true,
            "section_type": "core",
            "what_core_repository": "Repo here",
            "type_of_corer": "Corer type here",
            "depth_from_surface_to_start_of": "3",
            "total_core_length": "123",
            "location_locality": "Some locality here",
            "basin": "Some basin here",
            "age": "12345",
            "purpose": [
              "geochronology",
              "sequence_strat",
              "pleasure"
            ],
            "project_description": "Desc",
            "dates_of_work": "Dates here",
            "scale_of_interest": [
              "single_basin",
              "single_outcrop",
              "multi_basins",
              "single_core"
            ],
            "obs_interval_bed_obs_scale": "dm",
            "how_is_section_georeferenced": "point_at_secti",
            "strat_section_notes": "Some notes here"
          },
          "character": "package_succe",
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "mudstone",
              "mud_silt_grain_size": "clay",
              "relative_resistance_weather": "1",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "color_appearance": [
                "uniform",
                "patchy",
                "striped"
              ],
              "notes": "Notes here",
              "sand_grain_size": "sand_fine_low",
              "grain_size_range": [
                "sand_fine_low",
                "pebble",
                "pebble",
                "sand_medium_l"
              ],
              "congl_grain_size": "pebble",
              "breccia_grain_size": "pebble",
              "sand_fine_lower_percent": 12,
              "sand_medium_lower_percent": 23,
              "pebble_percent": 34,
              "maximum_clast_size_cm": 12,
              "minimum_clast_size_cm": 23,
              "average_clast_size_cm": 34,
              "matrix_size": [
                "silt",
                "none"
              ],
              "character": [
                "matrix-support",
                "imbrication"
              ],
              "sorting": [
                "well_sorted",
                "mod_sorted"
              ],
              "rounding": [
                "rounded",
                "very_angular"
              ],
              "shape": [
                "spherical",
                "equant"
              ],
              "minerals_present": [
                "quartz",
                "halite",
                "calcite",
                "chert",
                "rip_up_clasts"
              ],
              "sandstone_type_dott": [
                "quartz_arenite",
                "arkosic_arenit"
              ],
              "sandstone_type_folk_mcbride": [
                "quartzarenite",
                "subarkose",
                "sublitharenite"
              ],
              "sandstone_modifier": [
                "rip_up_clasts",
                "wood"
              ],
              "skeletal_carbonate_components": [
                "mollusc",
                "calcareous_alg",
                "brachiopod"
              ],
              "mollusc_percent": 12,
              "brachiopod_percent": 23,
              "calcareous_algae_percent": 34,
              "non_skeletal_carbonate_compone": [
                "mud",
                "oncoid",
                "pisoid"
              ],
              "mud_percent": 12,
              "oncoid_percent": 23,
              "pisoid_percent": 34,
              "clay_or_mudstone_type": [
                "red_mudstone",
                "siliceous_calc"
              ],
              "siliceous_calcareous_mudstone_percent": 12,
              "red_mudstone_percent": 23,
              "conglomerate_composition": [
                "extraformation",
                "monomictic"
              ],
              "clast_composition": [
                "igneous_clast",
                "conglomerate",
                "schist"
              ],
              "conglomerate_clast_percent": 12,
              "matrix_composition": [
                "conglomerate",
                "extrusive_igneous"
              ],
              "extrusive_igneous_matrix_percent": 23,
              "conglomerate_matrix_percent": 34,
              "volcaniclastic_type": [
                "glass"
              ],
              "glass_percent": 12,
              "evaporite_type": [
                "gyp_anhyd_dia"
              ],
              "gypsum_anhydrite_diagenetic_percent": 12,
              "gypsum_anhydrite_diagenetic_type": [
                "nodular_to_chi",
                "displacive"
              ],
              "phosphorite_type": [
                "nodular"
              ],
              "organic_coal_lithologies": [
                "peat",
                "coal_ball"
              ],
              "peat_percent": 12,
              "coal_ball_percent": 23
            }
          ],
          "bedding": {
            "thickness_of_individual_beds": 12,
            "package_bedding_trends": "uniform",
            "beds": [
              {
                "package_geometry": [
                  "discontinuous",
                  "tabular_parall"
                ],
                "shape_of_lower_contacts": [
                  "flat",
                  "irregular"
                ],
                "character_of_lower_contacts": [
                  "flat",
                  "undulatory"
                ],
                "shape_of_upper_contacts": [
                  "undulatory",
                  "curved"
                ],
                "character_of_upper_contacts": [
                  "sharp",
                  "gradational"
                ],
                "upper_contact_relief": "Relief here",
                "notes": "Notes here"
              }
            ]
          },
          "structures": [
            {
              "massive_structureless": "yes",
              "cross_bedding_type": [
                "cross_bedding",
                "trough"
              ],
              "cross_bedding_height_cm": 12,
              "cross_bedding_width_cm": 23,
              "cross_bedding_thickness_cm": 34,
              "cross_bedding_spacing_cm": 45,
              "ripple_lamination_type": [
                "cross_lamin",
                "lenticular"
              ],
              "ripple_lamination_height_mm": 12,
              "ripple_lamination_width_mm": 23,
              "ripple_lamination_thick_mm": 23,
              "ripple_lamination_spacing_mm": 34,
              "horizontal_bedding_type": [
                "horizontal",
                "planar"
              ],
              "graded_bedding_type": "normally_grade",
              "deformation_structures": [
                "contorted_bedd",
                "dikes"
              ],
              "lag_type": [
                "lag_deposit",
                "rip_up_clasts"
              ],
              "clast_composition": "Comp",
              "clast_size": "12",
              "layer_thickness_shape": "23",
              "other_common_structures": [
                "bouma_sequence"
              ],
              "bouma_sequence_part": [
                "a"
              ],
              "notes": "Notes here",
              "bioturbation_index": "1_sparse",
              "bedding_plane_features": [
                "bedforms",
                "gutter_cast"
              ],
              "bedding_plane_features_scale": "12",
              "bedform_type": [
                "wave_ripples",
                "3d_crests",
                "ladderback"
              ],
              "bedding_plane_features_orientation": "12",
              "bedform_scale": "23",
              "crest_orientation_azimuth_0_360": "45",
              "paleosol_horizons": [
                "o",
                "c"
              ],
              "o_horizon_thickness_cm": 12,
              "c_horizon_thickness_cm": 23,
              "paleosol_structures": [
                "peds",
                "leaching_horiz"
              ],
              "additional_modifiers": "Additional here",
              "paleosol_classification": [
                "gelisol",
                "histosol"
              ]
            }
          ],
          "diagenesis": [
            {
              "cement_composition": [
                "calcite",
                "clay"
              ],
              "vein_type": "parallel",
              "vein_width": 12,
              "vein_length": 23,
              "vein_orientation": "45",
              "vein_mineralogy": "iron_oxides",
              "fracture_type": "oblique",
              "fracture_width": 12,
              "fracture_length": 23,
              "fracture_orientation": "Or",
              "fracture_mineralogy": "evaporite_min",
              "nodules_concretions_size": "mm",
              "min": 12,
              "max": 45,
              "average": 55,
              "nodules_concretions_shape": [
                "spherical",
                "irregular"
              ],
              "spacing": 33,
              "nodules_concretions_type": "layered",
              "nodules_concretions_comp": [
                "calcite",
                "gypsum_anhydri"
              ],
              "replacement_type": "fossil_selecti",
              "recrystallization_type": "local",
              "other_diagenetic_features": [
                "stylolites",
                "liesegang_band"
              ],
              "fabric_selective": [
                "interparticle",
                "intraparticle"
              ],
              "non_selective": [
                "channel",
                "vug"
              ],
              "carbonate_desicc_and_diss": [
                "grykes",
                "sheet_cracks"
              ],
              "notes": "Notes here"
            }
          ],
          "fossils": [
            {
              "invertebrate": [
                "porifera_spong",
                "cnidaria",
                "chordata",
                "mollusca"
              ],
              "mollusca": [
                "cephalopod",
                "belemnite"
              ],
              "chordate": "tunicate",
              "plant_algae": [
                "red_algae",
                "phylloid"
              ],
              "vertebrate": [
                "chondrichthyes",
                "aves"
              ],
              "faunal_assemblage": "heterozoan",
              "diversity": "medium",
              "descriptive": [
                "track",
                "sub_vertical"
              ],
              "burrow_fill_type": [
                "mudstone",
                "active"
              ],
              "behavioral_grouping": [
                "locomotion",
                "farming"
              ],
              "ichnofacies": "skolithos",
              "list_of_specific_types": "Types here",
              "dominant_component": "microbial_reef",
              "other_dominant_component": "Other dom here",
              "microbial_reef_or_skelatal_mic": [
                "micro_laminate",
                "tufa"
              ],
              "other_microbial_or_skeletal_mi": "Other mic here",
              "height": "12",
              "width": "23",
              "orientation_if_elongate_azimu": 45,
              "shape": "dome",
              "type": "fringing",
              "accessory_structures": [
                "fenestrae",
                "geopetal"
              ],
              "notes": "Notes here"
            }
          ],
          "interpretations": [
            {
              "sediment_transport": [
                "waves",
                "turbidity_curr"
              ],
              "fluidization": "liquefaction",
              "miscellaneous": [
                "ice_rafting",
                "desiccation"
              ],
              "notes": "Notes here",
              "general": [
                "continental",
                "transitional"
              ],
              "clastic": [
                "playa",
                "glacial_and_pr"
              ],
              "glacial_and_proglacial_environ": [
                "till",
                "outwash"
              ],
              "carbonates": [
                "factory"
              ],
              "factory": [
                "photozoan",
                "metozoan"
              ],
              "geometry": "undulatory",
              "relief_scale": "cm",
              "extent": "23",
              "extent_scale": "m",
              "relief": "12",
              "type": [
                "mineralization",
                "pedogenic"
              ],
              "stratal_termination": "toplap",
              "general_surfaces": "Gen surf",
              "sequence_stratigraphic_surfaces": "type_3_sequenc",
              "named": "Named here",
              "description": [
                "fining_upward",
                "isolated"
              ],
              "stacking_sequence_stratigraphy": [
                "progradational",
                "highstand_syst"
              ],
              "fluvial_architectural_elements": [
                "gravelly_bar_o",
                "sandy_bedform"
              ],
              "lacustrine_architecture_interpretation": [
                "overfilled",
                "balanced"
              ],
              "carbonate_platform_geometry": [
                "attached",
                "unrimmed_platf"
              ],
              "deep_water_architctural_element": [
                "levee",
                "sheet"
              ],
              "carbonate_margin_geometry": [
                "accretionary_m",
                "other"
              ],
              "other_carbonate_margin_geometry": "Other geometry"
            }
          ]
        },
        "samples": [
          {
            "sample_type": "field",
            "id": 16530015451321,
            "sample_id_name": "Efg345",
            "label": "Sample1",
            "main_sampling_purpose": "geochronology",
            "deposit_thickness": "23",
            "sample_description": "Samp desc here",
            "material_type": "sediment",
            "inplaceness_of_sample": "5___definitely",
            "oriented_sample": "yes",
            "sample_orientation_notes": "Notes here",
            "sample_size": "123",
            "degree_of_weathering": "4",
            "sample_notes": "Some notes"
          }
        ],
        "gps_accuracy": 1.23,
        "name": "Spot1",
        "time": "2022-06-19T22:27:11.000Z",
        "id": 16529992313378,
        "pet": {
          "volcanic_rock_type": [
            "latite"
          ],
          "igneous_rock_class": [
            "volcanic"
          ],
          "rock_type": [
            "igneous"
          ],
          "occurence_volcanic": [
            "dome",
            "unclear"
          ],
          "texture_volcanic": [
            "clastic",
            "aphanitic"
          ],
          "color_index_volc": 23,
          "color_index_source_volc": "strabotools",
          "vol_characteristic_size_of_cry": 123,
          "structure_volcanic": [
            "eutaxitic"
          ],
          "alteration_volcanic": [
            "metamorphic_ov"
          ],
          "notes_volcanic": "Notes here",
          "minerals": [
            {
              "id": 16530034561873,
              "full_mineral_name": "Zircon",
              "mineral_abbrev": "zrn",
              "habit": "acicular",
              "textural_setting_igneous": [
                "phenocryst",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 12,
              "maximum_grain_size_mm": 23,
              "modal": 34,
              "mineral_notes": "Mineral notes here"
            },
            {
              "id": 16530035059185,
              "full_mineral_name": "Aegirine",
              "mineral_abbrev": "aeg",
              "habit": "euhedral",
              "textural_setting_igneous": [
                "vesicle",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 1,
              "maximum_grain_size_mm": 2,
              "modal": 3,
              "mineral_notes": "Notes here"
            }
          ],
          "reactions": [
            {
              "id": 16530035338583,
              "reactions": "Ab=zn+bc",
              "based_on": [
                "corona",
                "mineral_degrad"
              ],
              "notes": "Notes here"
            }
          ]
        },
        "spot_radius": 1.3,
        "self": "https://strabospot.org/db/feature/16529992313378"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -97.679878,
          38.576911
        ]
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0,
              0
            ],
            [
              0,
              80
            ],
            [
              20,
              80
            ],
            [
              20,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-05-19T23:11:15.000Z",
        "altitude": 405.94,
        "lng": -97.679578,
        "strat_section_id": 16530017020988,
        "surface_feature": {
          "surface_feature_type": "strat_interval"
        },
        "modified_timestamp": 1653001875459,
        "sed": {
          "character": "bed",
          "interval": {
            "interval_thickness": 4,
            "thickness_units": "m"
          },
          "bedding": {
            "beds": [
              {
                "notes": "Notes here"
              }
            ]
          },
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "siltstone",
              "mud_silt_grain_size": "silt",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "relative_resistance_weather": "3",
              "notes": "Notes here"
            }
          ]
        },
        "name": "Abc123",
        "time": "2022-05-19T23:11:15.000Z",
        "id": 16530018754410,
        "lat": 38.577,
        "self": "https://strabospot.org/db/feature/16530018754410"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Point",
        "coordinates": [
          2705.0625,
          1775.8125
        ]
      },
      "properties": {
        "date": "2022-08-10T16:29:43.000Z",
        "lng": -97.679878,
        "image_basemap": 16530015128805,
        "name": "On image",
        "time": "2022-08-10T16:29:43.000Z",
        "id": 16601489837307,
        "lat": 38.576911,
        "modified_timestamp": 1660148995221,
        "self": "https://strabospot.org/db/feature/16601489837307"
      },
      "type": "Feature"
    }
  ]
}

```
</details>

### (2) Multiple FeatureCollections
<details>
<summary>Request body ([FeatureCollection, ...])</summary>

```json
[{
  "type": "FeatureCollection",
  "features": [
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -97.676182,
              38.578769
            ],
            [
              -97.674251,
              38.579943
            ],
            [
              -97.6735,
              38.578198
            ],
            [
              -97.676182,
              38.578769
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:43.000Z",
        "name": "Abc126",
        "time": "2022-08-10T16:30:43.000Z",
        "id": 16601490430653,
        "modified_timestamp": 1660149043065,
        "self": "https://strabospot.org/db/feature/16601490430653"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            -97.679658,
            38.578886
          ],
          [
            -97.674508,
            38.576907
          ],
          [
            -97.671762,
            38.578484
          ]
        ]
      },
      "properties": {
        "date": "2022-08-10T16:30:34.000Z",
        "name": "Abc125",
        "time": "2022-08-10T16:30:34.000Z",
        "id": 16601490340852,
        "modified_timestamp": 1660149034086,
        "self": "https://strabospot.org/db/feature/16601490340852"
      },
      "type": "Feature"
    },
    {
      "properties": {
        "images": [
          {
            "width": 4032,
            "caption": "Image description here",
            "id": 16530015128805,
            "title": "My image",
            "annotated": true,
            "height": 3024,
            "image_type": "photo",
            "self": "https://strabospot.org/db/image/16530015128805"
          }
        ],
        "date": "2022-06-19T22:27:11.000Z",
        "altitude": 23,
        "notes": "Spot notes here",
        "data": {
          "urls": [
            "http://www.google.com"
          ]
        },
        "other_features": [
          {
            "id": 16530016041795,
            "label": "OthFeat",
            "type": "hydrologic",
            "name": "Feature Name",
            "description": "Desc here"
          }
        ],
        "orientation_data": [
          {
            "type": "planar_orientation",
            "id": 16529994975257,
            "label": "Plane1",
            "strike": 123,
            "dip_direction": 234,
            "dip": 45,
            "quality": "4",
            "feature_type": "fracture",
            "fracture_type": "opening_mode",
            "fracture_defined_by": "Something",
            "movement": "se_side_up",
            "movement_justification": [
              "not_specified",
              "offset_foliation"
            ],
            "directional_indicators": [
              "riedel_shear",
              "slickenfibers"
            ],
            "thickness": 2,
            "length": 3,
            "notes": "Pl feat notes"
          },
          {
            "type": "linear_orientation",
            "id": 16529995763665,
            "label": "Line1",
            "trend": 12,
            "plunge": 23,
            "rake": 34,
            "rake_calculated": "no",
            "quality": "3",
            "feature_type": "z_fold",
            "defined_by": "Something",
            "notes": "Notes here"
          },
          {
            "type": "tabular_orientation",
            "id": 16529996088030,
            "label": "Tab zone 1",
            "strike": 23,
            "dip_direction": 45,
            "dip": 55,
            "quality": "3",
            "feature_type": "vein",
            "vein_type": "normal_opening",
            "vein_fill": "quartz",
            "thickness": 23,
            "tabularity": "semi_constant",
            "length": 23,
            "defined_by": "Something here",
            "notes": "Tab notes"
          },
          {
            "type": "linear_orientation",
            "id": 16590144068585,
            "label": "Line2",
            "trend": 44,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144221415,
            "label": "line3",
            "trend": 55,
            "plunge": 66,
            "rake": 77,
            "rake_calculated": "no"
          },
          {
            "type": "linear_orientation",
            "id": 16590144415915,
            "label": "line4",
            "trend": 11,
            "plunge": 22,
            "rake": 33,
            "rake_calculated": "no"
          }
        ],
        "modified_timestamp": 1660148979966,
        "_3d_structures": [
          {
            "type": "fabric",
            "id": 16529996735747,
            "feature_type": "tectonite",
            "tectonite_type": "sl_tectonite",
            "tectonite_character": "s___l",
            "struct_notes": "Fab notes",
            "label": "tectonite"
          },
          {
            "type": "tensor",
            "id": 16529997746294,
            "label": "Tensor1",
            "feature_type": "non_ellipsoidal_data",
            "non_ellipsoidal_type": "flow_apophyses",
            "nonellipsoidal_max_value": 23,
            "nonellipsoidal_max_value_uncer": 43,
            "nonellipsoidal_max_trend": 56,
            "nonellipsoidal_max_trend_uncer": 34,
            "nonellipsoidal_max_plunge": 23,
            "nonellipsoidal_max_plunge_unce": 54,
            "nonellipsoidal_int_value": 23,
            "nonellipsoidal_int_value_uncer": 32,
            "nonellipsoidal_int_trend": 45,
            "nonellipsoidal_int_uncertainty": 34,
            "nonellipsoidal_int_plunge": 56,
            "nonellipsoidal_int_plunge_unce": 34,
            "nonellipsoidal_min_value": 23,
            "nonellipsoidal_min_value_uncer": 45,
            "nonellipsoidal_min_trend": 23,
            "nonellipsoidal_min_trend_uncer": 32,
            "nonellipsoidal_min_plunge": 23,
            "nonellipsoidal_min_plunge_unce": 45,
            "non_ellipsoidal_tensor_notes": "Notes here",
            "nonellipsoidal_quality_of_meas": "4",
            "struct_notes": "Tensor notes"
          },
          {
            "type": "other",
            "id": 16529998349655,
            "label": "Other1",
            "feature_type": "boudinage",
            "boudinage_geometry": "unidirectional",
            "boudinage_shape": "symmetrical",
            "boudinage_competent": "Mat",
            "boudinage_incompetent": "Mat",
            "average_width_of_boudin_neck": 34,
            "number_of_necks_measured": 3,
            "boudinage_wavelength_m": 4,
            "boudinaged_layer_thickness_m": 6,
            "boudinage_strike": 23,
            "boudinage_dip_direction": 34,
            "boudinage_dip": 56,
            "boudinage_trend": 23,
            "boudinage_plunge": 43,
            "boudinage_trend_uncertainty": 32,
            "boudinage_2nd_trend": 23,
            "boudinage_2nd_plunge": 34,
            "boudinage_2nd_trend_uncertaint": 12,
            "struct_notes": "Notes"
          },
          {
            "type": "fold",
            "id": 16529996884051,
            "label": "Fold1",
            "feature_type": "monocline",
            "Trend": 23,
            "Plunge": 34,
            "Linearity": "4",
            "Measurement_Quality": "4",
            "Strike": 12,
            "Azimuthal_Dip_Direction": 34,
            "Dip": 32,
            "Planarity": "3",
            "Measurement_Quality_001": "5___excellent",
            "fold_attitude": "vertical",
            "fold_shape": "class_1b__para",
            "tightness": "tight",
            "Hinge_Shape": "subrounded",
            "vergence": "south",
            "wavelength_m": 12,
            "amplitude_m": 23,
            "competent_material_fold": "Mat here",
            "folded_layer_thickness_m": 55,
            "incompetent_material_fold": "Mat here",
            "fold_fol_strike": 12,
            "fold_fol_dip_direction": 23,
            "fold_fol_dip": 34,
            "fold_fol_quality": "approximate",
            "fold_foliation_Type": "axial_planar",
            "fold_foliation_description": "Desc here",
            "fold_notes": "Fold notes here"
          }
        ],
        "fabrics": [
          {
            "type": "fault_rock",
            "id": 16530036019286,
            "label": "Fabric1",
            "inco_nofol": "fault_breccia",
            "inco_nofo_char": "Fab",
            "inco_fol": "foliated_gouge",
            "inco_fo_char": "Fab",
            "co_nofol": "cata",
            "co_nofo_char": "Fab",
            "co_fol": "fol_ultracata",
            "tectonite_type": "s>>l",
            "co_fo_char": "Fab",
            "structural_fabric": [
              "folding",
              "comp_banding"
            ],
            "char_fold": "Fold",
            "comp_band_min": "Zen",
            "spatial_config": [
              "planar",
              "anastomosing"
            ],
            "desc_spat_char": "Desc",
            "kin_ind_present": "yes_kin",
            "kinematic_fab": [
              "oblique_fabric",
              "asymm_fold"
            ],
            "grain_shape_char": "Zrn",
            "asym_fold_char": "Char",
            "sense_of_shear": "Top",
            "interp_note": "Notes"
          },
          {
            "type": "igneous_rock",
            "id": 16530036980941,
            "label": "Fabric2",
            "planar_fab": [
              "no_p_fab",
              "other_p_fab"
            ],
            "lin_fab": [
              "none"
            ],
            "mag_tectonite": "l>s",
            "add_mag_fab": [
              "commingle",
              "mullions"
            ],
            "mag_commingle": "Comm",
            "mag_mullion": "Mull",
            "magmatic_str": [
              "no_mag_str",
              "plume_str"
            ],
            "solid_state_str": [
              "ss_fab",
              "anneal_sz"
            ],
            "char_ss_fab": "Sol",
            "char_ss_sz": "Shear",
            "addition_fab": [
              "structural",
              "other"
            ],
            "str_fab": [
              "folding",
              "fractures"
            ],
            "fold_char": "Fold",
            "fracture_char": "Frac",
            "other_fab_char": "Other",
            "ss_tectonite": "ls",
            "mag_interp_note": "Notes"
          },
          {
            "type": "metamorphic_rock",
            "id": 16530037849501,
            "label": "Fabric3",
            "grain_size": "medium",
            "planar_fabric": [
              "gneissic_band",
              "schistosity"
            ],
            "plan_fab_min_1": "Min",
            "plan_fab_min_2": "Min",
            "plan_fab_min_3": "Min",
            "plan_fab_min_4": "Min",
            "spatial_var": "domainal",
            "length_scale": "Scale",
            "linear_fab": [
              "min_align_lin",
              "intersect_lin"
            ],
            "int_lin_char": "Planes",
            "other_met_fab": [
              "metasom",
              "migmatite"
            ],
            "metasomatic": "Min",
            "migmatitic": "Min",
            "additional_fab": [
              "structural",
              "relict_sed"
            ],
            "structural_fab": [
              "folding",
              "fault"
            ],
            "char_folding": "Char",
            "char_fault": "Char",
            "relict_sed_fab": [
              "bed",
              "flow_top_brecc"
            ],
            "kinematic_ind": "kin_yes",
            "kinematic_fab": [
              "asymm_fold",
              "bookshelf_slip",
              "sigmoidal_gash"
            ],
            "asym_fold_char": "Char",
            "book_slip_char": "Char",
            "sig_gash_char": "Char",
            "sense_of_shear": "Sense here",
            "tectonite_type": "ls",
            "p_t_d_history": "Hist here",
            "interp_note_meta": "Notes"
          }
        ],
        "sed": {
          "strat_section": {
            "strat_section_id": 16530017020988,
            "column_profile": "clastic",
            "column_y_axis_units": "m",
            "section_well_name": "Sec name here",
            "misc_labels": true,
            "display_lithology_patterns": true,
            "section_type": "core",
            "what_core_repository": "Repo here",
            "type_of_corer": "Corer type here",
            "depth_from_surface_to_start_of": "3",
            "total_core_length": "123",
            "location_locality": "Some locality here",
            "basin": "Some basin here",
            "age": "12345",
            "purpose": [
              "geochronology",
              "sequence_strat",
              "pleasure"
            ],
            "project_description": "Desc",
            "dates_of_work": "Dates here",
            "scale_of_interest": [
              "single_basin",
              "single_outcrop",
              "multi_basins",
              "single_core"
            ],
            "obs_interval_bed_obs_scale": "dm",
            "how_is_section_georeferenced": "point_at_secti",
            "strat_section_notes": "Some notes here"
          },
          "character": "package_succe",
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "mudstone",
              "mud_silt_grain_size": "clay",
              "relative_resistance_weather": "1",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "color_appearance": [
                "uniform",
                "patchy",
                "striped"
              ],
              "notes": "Notes here",
              "sand_grain_size": "sand_fine_low",
              "grain_size_range": [
                "sand_fine_low",
                "pebble",
                "pebble",
                "sand_medium_l"
              ],
              "congl_grain_size": "pebble",
              "breccia_grain_size": "pebble",
              "sand_fine_lower_percent": 12,
              "sand_medium_lower_percent": 23,
              "pebble_percent": 34,
              "maximum_clast_size_cm": 12,
              "minimum_clast_size_cm": 23,
              "average_clast_size_cm": 34,
              "matrix_size": [
                "silt",
                "none"
              ],
              "character": [
                "matrix-support",
                "imbrication"
              ],
              "sorting": [
                "well_sorted",
                "mod_sorted"
              ],
              "rounding": [
                "rounded",
                "very_angular"
              ],
              "shape": [
                "spherical",
                "equant"
              ],
              "minerals_present": [
                "quartz",
                "halite",
                "calcite",
                "chert",
                "rip_up_clasts"
              ],
              "sandstone_type_dott": [
                "quartz_arenite",
                "arkosic_arenit"
              ],
              "sandstone_type_folk_mcbride": [
                "quartzarenite",
                "subarkose",
                "sublitharenite"
              ],
              "sandstone_modifier": [
                "rip_up_clasts",
                "wood"
              ],
              "skeletal_carbonate_components": [
                "mollusc",
                "calcareous_alg",
                "brachiopod"
              ],
              "mollusc_percent": 12,
              "brachiopod_percent": 23,
              "calcareous_algae_percent": 34,
              "non_skeletal_carbonate_compone": [
                "mud",
                "oncoid",
                "pisoid"
              ],
              "mud_percent": 12,
              "oncoid_percent": 23,
              "pisoid_percent": 34,
              "clay_or_mudstone_type": [
                "red_mudstone",
                "siliceous_calc"
              ],
              "siliceous_calcareous_mudstone_percent": 12,
              "red_mudstone_percent": 23,
              "conglomerate_composition": [
                "extraformation",
                "monomictic"
              ],
              "clast_composition": [
                "igneous_clast",
                "conglomerate",
                "schist"
              ],
              "conglomerate_clast_percent": 12,
              "matrix_composition": [
                "conglomerate",
                "extrusive_igneous"
              ],
              "extrusive_igneous_matrix_percent": 23,
              "conglomerate_matrix_percent": 34,
              "volcaniclastic_type": [
                "glass"
              ],
              "glass_percent": 12,
              "evaporite_type": [
                "gyp_anhyd_dia"
              ],
              "gypsum_anhydrite_diagenetic_percent": 12,
              "gypsum_anhydrite_diagenetic_type": [
                "nodular_to_chi",
                "displacive"
              ],
              "phosphorite_type": [
                "nodular"
              ],
              "organic_coal_lithologies": [
                "peat",
                "coal_ball"
              ],
              "peat_percent": 12,
              "coal_ball_percent": 23
            }
          ],
          "bedding": {
            "thickness_of_individual_beds": 12,
            "package_bedding_trends": "uniform",
            "beds": [
              {
                "package_geometry": [
                  "discontinuous",
                  "tabular_parall"
                ],
                "shape_of_lower_contacts": [
                  "flat",
                  "irregular"
                ],
                "character_of_lower_contacts": [
                  "flat",
                  "undulatory"
                ],
                "shape_of_upper_contacts": [
                  "undulatory",
                  "curved"
                ],
                "character_of_upper_contacts": [
                  "sharp",
                  "gradational"
                ],
                "upper_contact_relief": "Relief here",
                "notes": "Notes here"
              }
            ]
          },
          "structures": [
            {
              "massive_structureless": "yes",
              "cross_bedding_type": [
                "cross_bedding",
                "trough"
              ],
              "cross_bedding_height_cm": 12,
              "cross_bedding_width_cm": 23,
              "cross_bedding_thickness_cm": 34,
              "cross_bedding_spacing_cm": 45,
              "ripple_lamination_type": [
                "cross_lamin",
                "lenticular"
              ],
              "ripple_lamination_height_mm": 12,
              "ripple_lamination_width_mm": 23,
              "ripple_lamination_thick_mm": 23,
              "ripple_lamination_spacing_mm": 34,
              "horizontal_bedding_type": [
                "horizontal",
                "planar"
              ],
              "graded_bedding_type": "normally_grade",
              "deformation_structures": [
                "contorted_bedd",
                "dikes"
              ],
              "lag_type": [
                "lag_deposit",
                "rip_up_clasts"
              ],
              "clast_composition": "Comp",
              "clast_size": "12",
              "layer_thickness_shape": "23",
              "other_common_structures": [
                "bouma_sequence"
              ],
              "bouma_sequence_part": [
                "a"
              ],
              "notes": "Notes here",
              "bioturbation_index": "1_sparse",
              "bedding_plane_features": [
                "bedforms",
                "gutter_cast"
              ],
              "bedding_plane_features_scale": "12",
              "bedform_type": [
                "wave_ripples",
                "3d_crests",
                "ladderback"
              ],
              "bedding_plane_features_orientation": "12",
              "bedform_scale": "23",
              "crest_orientation_azimuth_0_360": "45",
              "paleosol_horizons": [
                "o",
                "c"
              ],
              "o_horizon_thickness_cm": 12,
              "c_horizon_thickness_cm": 23,
              "paleosol_structures": [
                "peds",
                "leaching_horiz"
              ],
              "additional_modifiers": "Additional here",
              "paleosol_classification": [
                "gelisol",
                "histosol"
              ]
            }
          ],
          "diagenesis": [
            {
              "cement_composition": [
                "calcite",
                "clay"
              ],
              "vein_type": "parallel",
              "vein_width": 12,
              "vein_length": 23,
              "vein_orientation": "45",
              "vein_mineralogy": "iron_oxides",
              "fracture_type": "oblique",
              "fracture_width": 12,
              "fracture_length": 23,
              "fracture_orientation": "Or",
              "fracture_mineralogy": "evaporite_min",
              "nodules_concretions_size": "mm",
              "min": 12,
              "max": 45,
              "average": 55,
              "nodules_concretions_shape": [
                "spherical",
                "irregular"
              ],
              "spacing": 33,
              "nodules_concretions_type": "layered",
              "nodules_concretions_comp": [
                "calcite",
                "gypsum_anhydri"
              ],
              "replacement_type": "fossil_selecti",
              "recrystallization_type": "local",
              "other_diagenetic_features": [
                "stylolites",
                "liesegang_band"
              ],
              "fabric_selective": [
                "interparticle",
                "intraparticle"
              ],
              "non_selective": [
                "channel",
                "vug"
              ],
              "carbonate_desicc_and_diss": [
                "grykes",
                "sheet_cracks"
              ],
              "notes": "Notes here"
            }
          ],
          "fossils": [
            {
              "invertebrate": [
                "porifera_spong",
                "cnidaria",
                "chordata",
                "mollusca"
              ],
              "mollusca": [
                "cephalopod",
                "belemnite"
              ],
              "chordate": "tunicate",
              "plant_algae": [
                "red_algae",
                "phylloid"
              ],
              "vertebrate": [
                "chondrichthyes",
                "aves"
              ],
              "faunal_assemblage": "heterozoan",
              "diversity": "medium",
              "descriptive": [
                "track",
                "sub_vertical"
              ],
              "burrow_fill_type": [
                "mudstone",
                "active"
              ],
              "behavioral_grouping": [
                "locomotion",
                "farming"
              ],
              "ichnofacies": "skolithos",
              "list_of_specific_types": "Types here",
              "dominant_component": "microbial_reef",
              "other_dominant_component": "Other dom here",
              "microbial_reef_or_skelatal_mic": [
                "micro_laminate",
                "tufa"
              ],
              "other_microbial_or_skeletal_mi": "Other mic here",
              "height": "12",
              "width": "23",
              "orientation_if_elongate_azimu": 45,
              "shape": "dome",
              "type": "fringing",
              "accessory_structures": [
                "fenestrae",
                "geopetal"
              ],
              "notes": "Notes here"
            }
          ],
          "interpretations": [
            {
              "sediment_transport": [
                "waves",
                "turbidity_curr"
              ],
              "fluidization": "liquefaction",
              "miscellaneous": [
                "ice_rafting",
                "desiccation"
              ],
              "notes": "Notes here",
              "general": [
                "continental",
                "transitional"
              ],
              "clastic": [
                "playa",
                "glacial_and_pr"
              ],
              "glacial_and_proglacial_environ": [
                "till",
                "outwash"
              ],
              "carbonates": [
                "factory"
              ],
              "factory": [
                "photozoan",
                "metozoan"
              ],
              "geometry": "undulatory",
              "relief_scale": "cm",
              "extent": "23",
              "extent_scale": "m",
              "relief": "12",
              "type": [
                "mineralization",
                "pedogenic"
              ],
              "stratal_termination": "toplap",
              "general_surfaces": "Gen surf",
              "sequence_stratigraphic_surfaces": "type_3_sequenc",
              "named": "Named here",
              "description": [
                "fining_upward",
                "isolated"
              ],
              "stacking_sequence_stratigraphy": [
                "progradational",
                "highstand_syst"
              ],
              "fluvial_architectural_elements": [
                "gravelly_bar_o",
                "sandy_bedform"
              ],
              "lacustrine_architecture_interpretation": [
                "overfilled",
                "balanced"
              ],
              "carbonate_platform_geometry": [
                "attached",
                "unrimmed_platf"
              ],
              "deep_water_architctural_element": [
                "levee",
                "sheet"
              ],
              "carbonate_margin_geometry": [
                "accretionary_m",
                "other"
              ],
              "other_carbonate_margin_geometry": "Other geometry"
            }
          ]
        },
        "samples": [
          {
            "sample_type": "field",
            "id": 16530015451321,
            "sample_id_name": "Efg345",
            "label": "Sample1",
            "main_sampling_purpose": "geochronology",
            "deposit_thickness": "23",
            "sample_description": "Samp desc here",
            "material_type": "sediment",
            "inplaceness_of_sample": "5___definitely",
            "oriented_sample": "yes",
            "sample_orientation_notes": "Notes here",
            "sample_size": "123",
            "degree_of_weathering": "4",
            "sample_notes": "Some notes"
          }
        ],
        "gps_accuracy": 1.23,
        "name": "Spot1",
        "time": "2022-06-19T22:27:11.000Z",
        "id": 16529992313378,
        "pet": {
          "volcanic_rock_type": [
            "latite"
          ],
          "igneous_rock_class": [
            "volcanic"
          ],
          "rock_type": [
            "igneous"
          ],
          "occurence_volcanic": [
            "dome",
            "unclear"
          ],
          "texture_volcanic": [
            "clastic",
            "aphanitic"
          ],
          "color_index_volc": 23,
          "color_index_source_volc": "strabotools",
          "vol_characteristic_size_of_cry": 123,
          "structure_volcanic": [
            "eutaxitic"
          ],
          "alteration_volcanic": [
            "metamorphic_ov"
          ],
          "notes_volcanic": "Notes here",
          "minerals": [
            {
              "id": 16530034561873,
              "full_mineral_name": "Zircon",
              "mineral_abbrev": "zrn",
              "habit": "acicular",
              "textural_setting_igneous": [
                "phenocryst",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 12,
              "maximum_grain_size_mm": 23,
              "modal": 34,
              "mineral_notes": "Mineral notes here"
            },
            {
              "id": 16530035059185,
              "full_mineral_name": "Aegirine",
              "mineral_abbrev": "aeg",
              "habit": "euhedral",
              "textural_setting_igneous": [
                "vesicle",
                "vein"
              ],
              "textural_setting_metamorphic": [
                "phenocryst",
                "lineation_defi"
              ],
              "average_grain_size_mm": 1,
              "maximum_grain_size_mm": 2,
              "modal": 3,
              "mineral_notes": "Notes here"
            }
          ],
          "reactions": [
            {
              "id": 16530035338583,
              "reactions": "Ab=zn+bc",
              "based_on": [
                "corona",
                "mineral_degrad"
              ],
              "notes": "Notes here"
            }
          ]
        },
        "spot_radius": 1.3,
        "self": "https://strabospot.org/db/feature/16529992313378"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -97.679878,
          38.576911
        ]
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0,
              0
            ],
            [
              0,
              80
            ],
            [
              20,
              80
            ],
            [
              20,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "properties": {
        "date": "2022-05-19T23:11:15.000Z",
        "altitude": 405.94,
        "lng": -97.679578,
        "strat_section_id": 16530017020988,
        "surface_feature": {
          "surface_feature_type": "strat_interval"
        },
        "modified_timestamp": 1653001875459,
        "sed": {
          "character": "bed",
          "interval": {
            "interval_thickness": 4,
            "thickness_units": "m"
          },
          "bedding": {
            "beds": [
              {
                "notes": "Notes here"
              }
            ]
          },
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "siltstone",
              "mud_silt_grain_size": "silt",
              "lithification": "poorly_lithifi",
              "fresh_color": "Color",
              "weathered_color": "Color",
              "relative_resistance_weather": "3",
              "notes": "Notes here"
            }
          ]
        },
        "name": "Abc123",
        "time": "2022-05-19T23:11:15.000Z",
        "id": 16530018754410,
        "lat": 38.577,
        "self": "https://strabospot.org/db/feature/16530018754410"
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "Point",
        "coordinates": [
          2705.0625,
          1775.8125
        ]
      },
      "properties": {
        "date": "2022-08-10T16:29:43.000Z",
        "lng": -97.679878,
        "image_basemap": 16530015128805,
        "name": "On image",
        "time": "2022-08-10T16:29:43.000Z",
        "id": 16601489837307,
        "lat": 38.576911,
        "modified_timestamp": 1660148995221,
        "self": "https://strabospot.org/db/feature/16601489837307"
      },
      "type": "Feature"
    }
  ]
},
{
  "type": "FeatureCollection",
  "features": [
    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-97.676182, 38.578769],
            [-97.674251, 38.579943],
            [-97.673500, 38.578198],
            [-97.676182, 38.578769]
          ]
        ]
      },
      "properties": {
        "date": "2022-08-12T10:15:20.000Z",
        "name": "Abc226",
        "time": "2022-08-12T10:15:20.000Z",
        "id": 17601490430653,
        "modified_timestamp": 1660299320000,
        "self": "https://strabospot.org/db/feature/17601490430653"
      },
      "type": "Feature"
    },

    {
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [-97.679658, 38.578886],
          [-97.674508, 38.576907],
          [-97.671762, 38.578484]
        ]
      },
      "properties": {
        "date": "2022-08-12T10:14:10.000Z",
        "name": "Abc225",
        "time": "2022-08-12T10:14:10.000Z",
        "id": 17601490340852,
        "modified_timestamp": 1660299250000,
        "self": "https://strabospot.org/db/feature/17601490340852"
      },
      "type": "Feature"
    },

    {
      "properties": {
        "images": [
          {
            "width": 4096,
            "caption": "Alternate field view",
            "id": 17530015128806,
            "title": "My image 2",
            "annotated": false,
            "height": 3072,
            "image_type": "photo",
            "self": "https://strabospot.org/db/image/17530015128806"
          }
        ],
        "date": "2022-06-21T15:05:45.000Z",
        "altitude": 24,
        "notes": "Second spot: fresh fracture surface and subtle imbrication.",
        "data": {
          "urls": [
            "https://macrostrat.org",
            "http://example.com/resource"
          ]
        },
        "other_features": [
          {
            "id": 17530016041795,
            "label": "OthFeat-2",
            "type": "hydrologic",
            "name": "Small spring",
            "description": "Seep along contact"
          }
        ],
        "orientation_data": [
          {
            "type": "planar_orientation",
            "id": 17529994975257,
            "label": "Plane2",
            "strike": 135,
            "dip_direction": 225,
            "dip": 32,
            "quality": "3",
            "feature_type": "fracture",
            "fracture_type": "opening_mode",
            "fracture_defined_by": "trace",
            "movement": "nw_side_up",
            "movement_justification": ["not_specified"],
            "directional_indicators": ["slickenfibers"],
            "thickness": 1.5,
            "length": 2.2,
            "notes": "Clean surface"
          },
          {
            "type": "linear_orientation",
            "id": 17529995763665,
            "label": "LineA",
            "trend": 20,
            "plunge": 18,
            "rake": 25,
            "rake_calculated": "no",
            "quality": "3",
            "feature_type": "z_fold",
            "defined_by": "hinge",
            "notes": "Subtle"
          },
          {
            "type": "tabular_orientation",
            "id": 17529996088030,
            "label": "Tab zone 2",
            "strike": 30,
            "dip_direction": 60,
            "dip": 50,
            "quality": "3",
            "feature_type": "vein",
            "vein_type": "normal_opening",
            "vein_fill": "calcite",
            "thickness": 18,
            "tabularity": "semi_constant",
            "length": 21,
            "defined_by": "continuous",
            "notes": "Calcite-filled"
          }
        ],
        "modified_timestamp": 1660332345000,
        "_3d_structures": [
          {
            "type": "fabric",
            "id": 17529996735747,
            "feature_type": "tectonite",
            "tectonite_type": "sl_tectonite",
            "tectonite_character": "s___l",
            "struct_notes": "Weak S>>L overprint",
            "label": "tectonite-2"
          },
          {
            "type": "tensor",
            "id": 17529997746294,
            "label": "Tensor2",
            "feature_type": "non_ellipsoidal_data",
            "non_ellipsoidal_type": "flow_apophyses",
            "nonellipsoidal_max_value": 25,
            "nonellipsoidal_max_value_uncer": 40,
            "nonellipsoidal_max_trend": 60,
            "nonellipsoidal_max_trend_uncer": 30,
            "nonellipsoidal_max_plunge": 20,
            "nonellipsoidal_max_plunge_unce": 45,
            "nonellipsoidal_int_value": 22,
            "nonellipsoidal_int_value_uncer": 30,
            "nonellipsoidal_int_trend": 42,
            "nonellipsoidal_int_uncertainty": 28,
            "nonellipsoidal_int_plunge": 50,
            "nonellipsoidal_int_plunge_unce": 33,
            "nonellipsoidal_min_value": 18,
            "nonellipsoidal_min_value_uncer": 38,
            "nonellipsoidal_min_trend": 28,
            "nonellipsoidal_min_trend_uncer": 26,
            "nonellipsoidal_min_plunge": 18,
            "nonellipsoidal_min_plunge_unce": 40,
            "non_ellipsoidal_tensor_notes": "Comparable to nearby station",
            "nonellipsoidal_quality_of_meas": "3",
            "struct_notes": "Notes updated"
          }
        ],
        "fabrics": [
          {
            "type": "fault_rock",
            "id": 17530036019286,
            "label": "FabricA",
            "inco_nofol": "fault_breccia",
            "inco_nofo_char": "Angular fragments",
            "inco_fol": "foliated_gouge",
            "inco_fo_char": "Sheared clay",
            "co_nofol": "cata",
            "co_nofo_char": "Milled grains",
            "co_fol": "fol_ultracata",
            "tectonite_type": "s>>l",
            "co_fo_char": "Ultracataclasite bands",
            "structural_fabric": ["folding", "comp_banding"],
            "char_fold": "Open",
            "comp_band_min": "Qz",
            "spatial_config": ["planar", "anastomosing"],
            "desc_spat_char": "Interconnected bands",
            "kin_ind_present": "yes_kin",
            "kinematic_fab": ["oblique_fabric"],
            "grain_shape_char": "Subangular",
            "asym_fold_char": "Weak",
            "sense_of_shear": "Top-to-SE",
            "interp_note": "Localized"
          }
        ],
        "sed": {
          "strat_section": {
            "strat_section_id": 17530017020988,
            "column_profile": "clastic",
            "column_y_axis_units": "m",
            "section_well_name": "Sec name here",
            "misc_labels": true,
            "display_lithology_patterns": true,
            "section_type": "core",
            "what_core_repository": "Repo here",
            "type_of_corer": "Wireline",
            "depth_from_surface_to_start_of": "4",
            "total_core_length": "118",
            "location_locality": "Locality B",
            "basin": "Another basin",
            "age": "12346",
            "purpose": ["geochronology", "sequence_strat"],
            "project_description": "Desc 2",
            "dates_of_work": "Dates 2",
            "scale_of_interest": ["single_outcrop", "single_core"],
            "obs_interval_bed_obs_scale": "dm",
            "how_is_section_georeferenced": "point_at_secti",
            "strat_section_notes": "Alt notes"
          },
          "character": "package_succe",
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "mudstone",
              "mud_silt_grain_size": "clay",
              "relative_resistance_weather": "2",
              "lithification": "poorly_lithifi",
              "fresh_color": "Brown",
              "weathered_color": "Light brown",
              "color_appearance": ["uniform", "striped"],
              "notes": "Variably bioturbated",
              "sand_grain_size": "sand_fine_low",
              "grain_size_range": ["sand_fine_low", "sand_medium_l"],
              "congl_grain_size": "pebble",
              "breccia_grain_size": "pebble",
              "sand_fine_lower_percent": 10,
              "sand_medium_lower_percent": 20,
              "pebble_percent": 25,
              "maximum_clast_size_cm": 10,
              "minimum_clast_size_cm": 20,
              "average_clast_size_cm": 28,
              "matrix_size": ["silt"],
              "character": ["matrix-support"],
              "sorting": ["mod_sorted"],
              "rounding": ["rounded", "subangular"],
              "shape": ["equant"],
              "minerals_present": ["quartz", "calcite", "chert"],
              "sandstone_type_dott": ["quartz_arenite"],
              "sandstone_type_folk_mcbride": ["quartzarenite"],
              "sandstone_modifier": ["wood"],
              "skeletal_carbonate_components": ["mollusc"],
              "mollusc_percent": 8,
              "non_skeletal_carbonate_compone": ["mud"],
              "mud_percent": 15
            }
          ]
        },
        "samples": [
          {
            "sample_type": "field",
            "id": 17530015451321,
            "sample_id_name": "Hij678",
            "label": "Sample2",
            "main_sampling_purpose": "geochronology",
            "deposit_thickness": "18",
            "sample_description": "Fine mudstone with plant debris",
            "material_type": "sediment",
            "inplaceness_of_sample": "4___probable",
            "oriented_sample": "no",
            "sample_orientation_notes": "NA",
            "sample_size": "110",
            "degree_of_weathering": "3",
            "sample_notes": "Collected from fresh surface"
          }
        ],
        "gps_accuracy": 2.5,
        "name": "Spot2",
        "time": "2022-06-21T15:05:45.000Z",
        "id": 17529992313379,
        "pet": {
          "volcanic_rock_type": ["trachyte"],
          "igneous_rock_class": ["volcanic"],
          "rock_type": ["igneous"],
          "occurence_volcanic": ["flow", "unclear"],
          "texture_volcanic": ["aphanitic"],
          "color_index_volc": 18,
          "color_index_source_volc": "strabotools",
          "vol_characteristic_size_of_cry": 95,
          "structure_volcanic": ["eutaxitic"],
          "alteration_volcanic": ["propylitic"],
          "notes_volcanic": "Weak alteration halos",
          "minerals": [
            {
              "id": 17530034561873,
              "full_mineral_name": "Zircon",
              "mineral_abbrev": "zrn",
              "habit": "prismatic",
              "textural_setting_igneous": ["phenocryst"],
              "textural_setting_metamorphic": ["lineation_defi"],
              "average_grain_size_mm": 0.8,
              "maximum_grain_size_mm": 1.6,
              "modal": 2,
              "mineral_notes": "Sparse"
            }
          ],
          "reactions": [
            {
              "id": 17530035338583,
              "reactions": "Ab = An + Qtz",
              "based_on": ["textures"],
              "notes": "Tentative"
            }
          ]
        },
        "spot_radius": 1.6,
        "self": "https://strabospot.org/db/feature/17529992313379"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-97.679520, 38.577220]
      },
      "type": "Feature"
    },

    {
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [0, 0],
            [0, 80],
            [20, 80],
            [20, 0],
            [0, 0]
          ]
        ]
      },
      "properties": {
        "date": "2022-05-21T12:00:00.000Z",
        "altitude": 406.25,
        "lng": -97.679400,
        "strat_section_id": 17530017020988,
        "surface_feature": {
          "surface_feature_type": "strat_interval"
        },
        "modified_timestamp": 1653134400000,
        "sed": {
          "character": "bed",
          "interval": {
            "interval_thickness": 3.5,
            "thickness_units": "m"
          },
          "bedding": {
            "beds": [
              {
                "notes": "Subtle gradation upward"
              }
            ]
          },
          "lithologies": [
            {
              "primary_lithology": "siliciclastic",
              "siliciclastic_type": "siltstone",
              "mud_silt_grain_size": "silt",
              "lithification": "poorly_lithifi",
              "fresh_color": "Gray",
              "weathered_color": "Tan",
              "relative_resistance_weather": "3",
              "notes": "Ripple lamination present"
            }
          ]
        },
        "name": "Abc223",
        "time": "2022-05-21T12:00:00.000Z",
        "id": 17530018754411,
        "lat": 38.577200,
        "self": "https://strabospot.org/db/feature/17530018754411"
      },
      "type": "Feature"
    },

    {
      "geometry": {
        "type": "Point",
        "coordinates": [2705.0625, 1775.8125]
      },
      "properties": {
        "date": "2022-08-12T10:13:05.000Z",
        "lng": -97.679878,
        "image_basemap": 17530015128806,
        "name": "On image 2",
        "time": "2022-08-12T10:13:05.000Z",
        "id": 17601489837308,
        "lat": 38.576911,
        "modified_timestamp": 1660299185000,
        "self": "https://strabospot.org/db/feature/17601489837308"
      },
      "type": "Feature"
    }
  ]
}]

```
</details>

---

### Notes
- **Lat/Lng validation**: Points outside valid ranges are skipped.
- **Image basemaps** are ignored.
- `created` is parsed from `time` or `date` (ISO8601 or `"Month DD, YYYY"`); `updated` uses `modified_timestamp` if available.
- Planar orientation is extracted from the **first** `planar_orientation` item with numeric `strike` & `dip`.
