A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine via Remote Control API. Built with TypeScript and designed for game development automation.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/unreal-engine-mcp-server](https://hub.docker.com/repository/docker/mcp/unreal-engine-mcp-server)
**Author**|[ChiR24](https://github.com/ChiR24)
**Repository**|https://github.com/ChiR24/Unreal_mcp

## Available Tools (23)
Tools provided by this Server|Short Description
-|-
`animation_physics`|Author animation and physics assets: Animation Blueprints, blend spaces, montages, Control Rig/IK, skeletons, sockets, physics assets, cloth, ragdolls, and vehicles.|
`build_environment`|Build environments: landscapes, foliage, procedural terrain/biomes, lighting setups, spline roads/rivers/fences, and world decoration.|
`control_actor`|Spawn actors, set transforms, enable physics, add components, manage tags, and attach actors.|
`control_editor`|Start/stop PIE, control viewport camera, run console commands, take screenshots, simulate input.|
`inspect`|Inspect any UObject: read/write properties, list components, export snapshots, and query class info.|
`manage_ai`|Build AI systems: AI controllers, Behavior Trees, Blackboards, EQS, perception, State Trees, Smart Objects, NavMesh settings, nav modifiers, links, and pathfinding.|
`manage_asset`|Create/import/manage assets, material graphs, material instances, procedural textures, render targets, and dependency analysis.|
`manage_audio`|Play/stop sounds, add audio components, configure mixes, attenuation, spatial audio, and author Sound Cues/MetaSounds.|
`manage_blueprint`|Create Blueprints and UMG widgets, add SCS/UI components, set defaults, and manipulate Blueprint graphs, bindings, and widget layouts.|
`manage_character`|Create Character Blueprints with movement, locomotion, and animation state machines.|
`manage_combat`|Create weapons with hitscan/projectile firing, configure damage types, hitboxes, reload, and melee combat (combos, parry, block).|
`manage_effect`|Niagara particle systems, VFX, debug shapes, and GPU simulations.|
`manage_gas`|Create Gameplay Abilities, Effects, Attribute Sets, and Gameplay Cues for ability systems.|
`manage_geometry`|Create procedural meshes using Geometry Script: booleans, deformers, UVs, collision, and LOD generation.|
`manage_interaction`|Create interactive objects: doors, switches, chests, levers.|
`manage_inventory`|Create item data assets, inventory components, world pickups, loot tables, and crafting recipes.|
`manage_level`|Load/save levels, configure streaming, and build lighting.|
`manage_level_structure`|Structure worlds: levels, sublevels, World Partition, streaming, data layers, HLOD, level instances, trigger/blocking/physics/audio/post-process volumes, and nav bounds.|
`manage_networking`|Configure multiplayer and player flow: replication, RPCs, authority/relevancy, network prediction, sessions, split-screen, LAN/voice chat, game framework classes, match rules, and input mappings.|
`manage_pcg`|Create, edit, execute, and configure PCG graphs: graph assets, input/sampler/filter/spawner nodes, pin connections, node settings, and partition grid size.|
`manage_sequence`|Edit Level Sequences: add tracks, bind actors, set keyframes, control playback, and record camera.|
`manage_tools`|Dynamic MCP tool management.|
`system_control`|Control the project runtime: profiling, benchmarks, scalability/LOD/Nanite settings, CVars, console commands, Python scripts, UBT, tests, logs, and widgets.|

---
## Tools Details

#### Tool: **`animation_physics`**
Author animation and physics assets: Animation Blueprints, blend spaces, montages, Control Rig/IK, skeletons, sockets, physics assets, cloth, ragdolls, and vehicles. Required: action. Select one enum value, then provide only parameters relevant to that action. Params by action: name, path, assetPath, animationPath, savePath, skeletonPath, parentClass, actorName, targetSkeleton, slotName, sectionName, notifyName, boneName, curveName, stateName, machineName, numFrames, frameRate, interpolationType, axisName, playRate, frame, time, length, location, rotation, scale, value, vehicleType, mass, dragCoefficient, artifacts, sourceSkeleton, sourceIKRigPath, targetIKRigPath, save, additiveAnimType, angularDamping, assets, assignToMesh, attachBoneName, axis, basePoseFrame, basePoseType, blendTime, blendType, blueprintPath, bodyA, bodyB, bodyType, boneTracks, cacheName, center, collisionEnabled, compileReferencers, constraintName, deltas, enableRootMotion, endFrame, forceRootLock, fromSection, fromState, layerSetup, limits, linearDamping, lodIndex, markerName, maxValue, minValue, montagePath, morphTargetName, morphTargetPath, newBoneName, nodeName, outputPath, overwrite, parentBoneName, physicsAssetName, physicsAssetPath, pitch, profileName, propertyName, radius, rebuildBlendParameters, relativeLocation, relativeRotation, relativeScale, removeChildren, rootBoneName, rootMotionRootLock, sampleValue, simulatePhysics, skeletalMeshPath, socketName, sourceBoneName, sourceChain, sourceMeshPath, startFrame, startTime, stateMachineName, suffix, targetBoneName, targetChain, targetMeshPath, threshold, toSection, toState, trackIndex, weights, yaw, params.
Parameters|Type|Description
-|-|-
`action`|`string`|Action
`actorName`|`string` *optional*|Name of the actor.
`additiveAnimType`|`string` *optional*|
`angularDamping`|`number` *optional*|
`animationPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`artifacts`|`array` *optional*|
`assetPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`assets`|`array` *optional*|
`assignToMesh`|`boolean` *optional*|
`attachBoneName`|`string` *optional*|Name of the bone.
`axis`|`string` *optional*|
`axisName`|`string` *optional*|
`basePoseFrame`|`number` *optional*|
`basePoseType`|`string` *optional*|
`blendTime`|`number` *optional*|
`blendType`|`string` *optional*|
`blueprintPath`|`string` *optional*|Blueprint asset path.
`bodyA`|`string` *optional*|
`bodyB`|`string` *optional*|
`bodyType`|`string` *optional*|
`boneName`|`string` *optional*|Name of the bone.
`boneTracks`|`array` *optional*|
`cacheName`|`string` *optional*|
`center`|`object` *optional*|3D location (x, y, z).
`collisionEnabled`|`boolean` *optional*|
`compileReferencers`|`boolean` *optional*|force_rebuild_blend_space: after rebuilding the BS, cascade-compile every AnimBlueprint that references it (via IAssetRegistry referencers). Response returns referencersCompiled count + compiledAnimBlueprints path list. Default true.
`constraintName`|`string` *optional*|
`curveName`|`string` *optional*|
`deltas`|`array` *optional*|
`dragCoefficient`|`number` *optional*|
`enableRootMotion`|`boolean` *optional*|
`endFrame`|`number` *optional*|
`forceRootLock`|`boolean` *optional*|
`frame`|`number` *optional*|
`frameRate`|`number` *optional*|
`fromSection`|`string` *optional*|
`fromState`|`string` *optional*|
`interpolationType`|`string` *optional*|
`layerSetup`|`array` *optional*|
`length`|`number` *optional*|
`limits`|`object` *optional*|
`linearDamping`|`number` *optional*|
`location`|`object` *optional*|3D location (x, y, z).
`lodIndex`|`number` *optional*|
`machineName`|`string` *optional*|
`markerName`|`string` *optional*|
`mass`|`number` *optional*|
`maxValue`|`number` *optional*|
`minValue`|`number` *optional*|
`montagePath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`morphTargetName`|`string` *optional*|
`morphTargetPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`name`|`string` *optional*|Name identifier.
`newBoneName`|`string` *optional*|Name of the bone.
`nodeName`|`string` *optional*|Name of the node.
`notifyName`|`string` *optional*|
`numFrames`|`number` *optional*|
`outputPath`|`string` *optional*|Output file or directory path.
`overwrite`|`boolean` *optional*|Overwrite if the asset/file already exists.
`params`|`object` *optional*|Optional action-specific parameters. These are merged with top-level arguments before routing for clients that cannot send arbitrary top-level fields.
`parentBoneName`|`string` *optional*|Name of the bone.
`parentClass`|`string` *optional*|
`path`|`string` *optional*|Directory path for asset creation.
`physicsAssetName`|`string` *optional*|
`physicsAssetPath`|`string` *optional*|Path to physics asset.
`pitch`|`number` *optional*|
`playRate`|`number` *optional*|
`profileName`|`string` *optional*|
`propertyName`|`string` *optional*|Name of the property.
`radius`|`number` *optional*|
`rebuildBlendParameters`|`boolean` *optional*|force_rebuild_blend_space: also trigger PostEditChangeProperty for the BlendParameters UPROPERTY (axis min/max changed). Default false.
`relativeLocation`|`object` *optional*|3D location (x, y, z).
`relativeRotation`|`object` *optional*|3D rotation (pitch, yaw, roll).
`relativeScale`|`object` *optional*|3D scale (x, y, z).
`removeChildren`|`boolean` *optional*|
`rootBoneName`|`string` *optional*|Name of the bone.
`rootMotionRootLock`|`string` *optional*|
`rotation`|`object` *optional*|3D rotation (pitch, yaw, roll).
`sampleValue`|`number` *optional*|
`save`|`boolean` *optional*|Save the asset(s) after the operation.
`savePath`|`string` *optional*|Path to save the asset.
`scale`|`object` *optional*|3D scale (x, y, z).
`sectionName`|`string` *optional*|
`simulatePhysics`|`boolean` *optional*|
`skeletalMeshPath`|`string` *optional*|Skeletal mesh path.
`skeletonPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`slotName`|`string` *optional*|
`socketName`|`string` *optional*|Name of the socket.
`sourceBoneName`|`string` *optional*|Name of the bone.
`sourceChain`|`string` *optional*|
`sourceIKRigPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`sourceMeshPath`|`string` *optional*|Mesh asset path.
`sourceSkeleton`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`startFrame`|`number` *optional*|
`startTime`|`number` *optional*|
`stateMachineName`|`string` *optional*|
`stateName`|`string` *optional*|
`suffix`|`string` *optional*|
`targetBoneName`|`string` *optional*|Name of the bone.
`targetChain`|`string` *optional*|
`targetIKRigPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`targetMeshPath`|`string` *optional*|Mesh asset path.
`targetSkeleton`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`threshold`|`number` *optional*|
`time`|`number` *optional*|
`toSection`|`string` *optional*|
`toState`|`string` *optional*|
`trackIndex`|`number` *optional*|
`value`|`string` *optional*|Generic value (any type).
`vehicleType`|`string` *optional*|
`weights`|`array` *optional*|
`yaw`|`number` *optional*|

---
#### Tool: **`build_environment`**
Build environments: landscapes, foliage, procedural terrain/biomes, lighting setups, spline roads/rivers/fences, and world decoration. Required: action. Select one enum value, then provide only parameters relevant to that action. Params by action: name, landscapeName, heightData, minX, minY, maxX, maxY, updateNormals, location, rotation, sizeX, sizeY, sectionSize, sectionsPerComponent, componentCount, materialPath, tool, radius, strength, falloff, layerName, actorName, foliageType, foliageTypePath, meshPath, density, minScale, maxScale, cullDistance, alignToNormal, randomYaw, removeAll, locations, transforms, position, bounds, volumeName, seed, foliageTypes, points, quadsPerSection, count, assets, numLODs, subdivisions, tileSize, quality, staticMesh, timeoutMs, path, filename, assetPaths, heightmapPath, outputPath, landscapePath, landscapeActorPath, actorPath, layerInfoPath, physicalMaterialPath, noWeightBlend, hardness, waterBodyName, targetActor, particleSystemPath, curvePath, cubemapPath, settings, waveHeight, waveLength, amplitude, steepness, speed, direction, azimuth, elevation, collisionEnabled, names, time, spacing, heightScale, material, hour, intensity, skyLightIntensity, alignToSpline, arriveTangent, bClosedLoop, blueprintPath, compensationValue, componentName, enabled, forwardAxis, initialPoints, leaveTangent, lightType, materialIndex, maxBrightness, method, minBrightness, operation, pointIndex, pointRotation, pointScale, pointType, propertyName, propertyValue, randomOffsetRange, randomizeRotation, randomizeScale, region, rotationRange, save, skipFlush, splineType, useRandomOffset, width, params.
Parameters|Type|Description
-|-|-
`action`|`string`|Action
`actorName`|`string` *optional*|Name of the actor.
`actorPath`|`string` *optional*|
`alignToNormal`|`boolean` *optional*|
`alignToSpline`|`boolean` *optional*|
`amplitude`|`number` *optional*|
`arriveTangent`|`object` *optional*|3D location (x, y, z).
`assetPaths`|`array` *optional*|
`assets`|`array` *optional*|
`azimuth`|`number` *optional*|
`bClosedLoop`|`boolean` *optional*|
`blueprintPath`|`string` *optional*|Blueprint asset path.
`bounds`|`object` *optional*|
`collisionEnabled`|`boolean` *optional*|
`compensationValue`|`number` *optional*|
`componentCount`|`object` *optional*|2D vector.
`componentName`|`string` *optional*|Name of the component.
`count`|`number` *optional*|
`cubemapPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`cullDistance`|`number` *optional*|
`curvePath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`density`|`number` *optional*|
`direction`|`object` *optional*|3D rotation (pitch, yaw, roll).
`elevation`|`number` *optional*|
`enabled`|`boolean` *optional*|Whether the item/feature is enabled.
`falloff`|`number` *optional*|
`filename`|`string` *optional*|
`foliageType`|`string` *optional*|
`foliageTypePath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`foliageTypes`|`array` *optional*|
`forwardAxis`|`string` *optional*|
`hardness`|`number` *optional*|
`heightData`|`array` *optional*|
`heightScale`|`number` *optional*|
`heightmapPath`|`string` *optional*|
`hour`|`number` *optional*|
`initialPoints`|`array` *optional*|
`intensity`|`number` *optional*|
`landscapeActorPath`|`string` *optional*|
`landscapeName`|`string` *optional*|
`landscapePath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`layerInfoPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`layerName`|`string` *optional*|
`leaveTangent`|`object` *optional*|3D location (x, y, z).
`lightType`|`string` *optional*|
`location`|`object` *optional*|3D location (x, y, z).
`locations`|`array` *optional*|
`material`|`string` *optional*|Material asset path.
`materialIndex`|`number` *optional*|
`materialPath`|`string` *optional*|Material asset path.
`maxBrightness`|`number` *optional*|
`maxScale`|`number` *optional*|
`maxX`|`number` *optional*|
`maxY`|`number` *optional*|
`meshPath`|`string` *optional*|Mesh asset path.
`method`|`string` *optional*|
`minBrightness`|`number` *optional*|
`minScale`|`number` *optional*|
`minX`|`number` *optional*|
`minY`|`number` *optional*|
`name`|`string` *optional*|Name identifier.
`names`|`array` *optional*|
`noWeightBlend`|`boolean` *optional*|
`numLODs`|`number` *optional*|
`operation`|`string` *optional*|
`outputPath`|`string` *optional*|
`params`|`object` *optional*|Optional action-specific parameters. These are merged with top-level arguments before routing for clients that cannot send arbitrary top-level fields.
`particleSystemPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`path`|`string` *optional*|Path to a directory.
`physicalMaterialPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`pointIndex`|`number` *optional*|
`pointRotation`|`object` *optional*|3D rotation (pitch, yaw, roll).
`pointScale`|`object` *optional*|3D scale (x, y, z).
`pointType`|`string` *optional*|
`points`|`array` *optional*|
`position`|`object` *optional*|3D location (x, y, z).
`propertyName`|`string` *optional*|Name of the property.
`propertyValue`|`string` *optional*|Generic value (any type).
`quadsPerSection`|`number` *optional*|
`quality`|`string` *optional*|
`radius`|`number` *optional*|
`randomOffsetRange`|`number` *optional*|
`randomYaw`|`boolean` *optional*|
`randomizeRotation`|`boolean` *optional*|
`randomizeScale`|`boolean` *optional*|
`region`|`object` *optional*|
`removeAll`|`boolean` *optional*|
`rotation`|`object` *optional*|3D rotation (pitch, yaw, roll).
`rotationRange`|`object` *optional*|3D rotation (pitch, yaw, roll).
`save`|`boolean` *optional*|Save the asset(s) after the operation.
`sectionSize`|`number` *optional*|
`sectionsPerComponent`|`number` *optional*|
`seed`|`number` *optional*|
`settings`|`object` *optional*|
`sizeX`|`number` *optional*|
`sizeY`|`number` *optional*|
`skipFlush`|`boolean` *optional*|
`skyLightIntensity`|`number` *optional*|
`spacing`|`number` *optional*|
`speed`|`number` *optional*|
`splineType`|`string` *optional*|
`staticMesh`|`string` *optional*|Mesh asset path.
`steepness`|`number` *optional*|
`strength`|`number` *optional*|
`subdivisions`|`number` *optional*|
`targetActor`|`string` *optional*|Name of the actor.
`tileSize`|`number` *optional*|
`time`|`number` *optional*|
`timeoutMs`|`number` *optional*|
`tool`|`string` *optional*|
`transforms`|`array` *optional*|
`updateNormals`|`boolean` *optional*|
`useRandomOffset`|`boolean` *optional*|
`volumeName`|`string` *optional*|
`waterBodyName`|`string` *optional*|Name of the actor.
`waveHeight`|`number` *optional*|
`waveLength`|`number` *optional*|
`width`|`number` *optional*|

---
#### Tool: **`control_actor`**
Spawn actors, set transforms, enable physics, add components, manage tags, and attach actors. Required: action. Select one enum value, then provide only parameters relevant to that action. Params by action: actorName, childActor, parentActor, classPath, meshPath, materialPath, materialSlot, materialIndex, allComponents, blueprintPath, location, rotation, scale, force, componentType, componentName, properties, visible, newName, tag, variables, snapshotName, actorClass, actorNames, arguments, className, collisionEnabled, functionName, limit, filter, name, offset, propertyName, value, params.
Parameters|Type|Description
-|-|-
`action`|`string`|Action
`actorClass`|`string` *optional*|
`actorName`|`string` *optional*|Name of the actor.
`actorNames`|`array` *optional*|
`allComponents`|`boolean` *optional*|
`arguments`|`string` *optional*|Generic value (any type).
`blueprintPath`|`string` *optional*|Blueprint asset path.
`childActor`|`string` *optional*|Name of the child actor (for attach/detach operations).
`className`|`string` *optional*|
`classPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`collisionEnabled`|`boolean` *optional*|
`componentName`|`string` *optional*|Name of the component.
`componentType`|`string` *optional*|
`filter`|`string` *optional*|
`force`|`object` *optional*|3D vector.
`functionName`|`string` *optional*|Name of the function.
`limit`|`number` *optional*|
`location`|`object` *optional*|3D location (x, y, z).
`materialIndex`|`integer` *optional*|
`materialPath`|`string` *optional*|Material asset path.
`materialSlot`|`integer` *optional*|
`meshPath`|`string` *optional*|Mesh asset path.
`name`|`string` *optional*|Name identifier.
`newName`|`string` *optional*|New name for renaming.
`offset`|`object` *optional*|3D location (x, y, z).
`params`|`object` *optional*|Optional action-specific parameters. These are merged with top-level arguments before routing for clients that cannot send arbitrary top-level fields.
`parentActor`|`string` *optional*|Name of the parent actor (for attach operations).
`properties`|`object` *optional*|
`propertyName`|`string` *optional*|Name of the property.
`rotation`|`object` *optional*|3D rotation (pitch, yaw, roll).
`scale`|`object` *optional*|3D scale (x, y, z).
`snapshotName`|`string` *optional*|
`tag`|`string` *optional*|Name of the tag.
`value`|`string` *optional*|Generic value (any type).
`variables`|`object` *optional*|
`visible`|`boolean` *optional*|Whether the item/actor is visible.

---
#### Tool: **`control_editor`**
Start/stop PIE, control viewport camera, run console commands, take screenshots, simulate input. Required: action. Select one enum value, then provide only parameters relevant to that action. Params by action: location, rotation, viewMode, enabled, speed, filename, fov, width, height, command, steps, bookmarkName, assetPath, path, levelPath, actorName, objectPath, name, blendTime, mode, returnBase64, includeMetadata, metadata, deltaTime, resolution, realtime, stat, category, preferences, key, type, inputType, inputAction, x, y, button, id, params.
Parameters|Type|Description
-|-|-
`action`|`string`|Editor action
`actorName`|`string` *optional*|Name of the actor.
`assetPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`blendTime`|`number` *optional*|
`bookmarkName`|`string` *optional*|
`button`|`string` *optional*|
`category`|`string` *optional*|
`command`|`string` *optional*|
`deltaTime`|`number` *optional*|
`enabled`|`boolean` *optional*|Whether the item/feature is enabled.
`filename`|`string` *optional*|
`fov`|`number` *optional*|
`height`|`number` *optional*|
`id`|`string` *optional*|
`includeMetadata`|`boolean` *optional*|
`inputAction`|`string` *optional*|
`inputType`|`string` *optional*|
`key`|`string` *optional*|
`levelPath`|`string` *optional*|Level asset path.
`location`|`object` *optional*|3D location (x, y, z).
`metadata`|`object` *optional*|
`mode`|`string` *optional*|Editor mode for set_editor_mode, or screenshot source: editor_viewport, game_viewport, full_editor_window.
`name`|`string` *optional*|Name identifier.
`objectPath`|`string` *optional*|
`params`|`object` *optional*|Optional action-specific parameters. These are merged with top-level arguments before routing for clients that cannot send arbitrary top-level fields.
`path`|`string` *optional*|Path to a directory.
`preferences`|`object` *optional*|
`realtime`|`boolean` *optional*|
`resolution`|`string` *optional*|Resolution setting (e.g., 1024x1024).
`returnBase64`|`boolean` *optional*|Return PNG image data as base64 when supported. Defaults to true for full_editor_window and game_viewport modes.
`rotation`|`object` *optional*|3D rotation (pitch, yaw, roll).
`speed`|`number` *optional*|
`stat`|`string` *optional*|
`steps`|`integer` *optional*|
`type`|`string` *optional*|
`viewMode`|`string` *optional*|
`width`|`number` *optional*|
`x`|`number` *optional*|
`y`|`number` *optional*|

---
#### Tool: **`inspect`**
Inspect any UObject: read/write properties, list components, export snapshots, and query class info. Actions: inspect_cdo (Blueprint CDO properties + all components without spawning an actor; use blueprintPath, optional detailed/componentName/propertyNames), inspect_class (class metadata), inspect_object (world actor), get_property/set_property, get_components, list_objects, find_by_class, find_by_tag, runtime_report. Required: action. Select one enum value, then provide only parameters relevant to that action. Params by action: objectPath, propertyName, propertyPath, value, actorName, name, componentName, className, classPath, tag, filter, snapshotName, blueprintPath, detailed, propertyNames, componentNames, params.
Parameters|Type|Description
-|-|-
`action`|`string`|Action
`actorName`|`string` *optional*|Name of the actor.
`blueprintPath`|`string` *optional*|Blueprint asset path.
`className`|`string` *optional*|
`classPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`componentName`|`string` *optional*|Name of the component.
`componentNames`|`array` *optional*|
`detailed`|`boolean` *optional*|
`filter`|`string` *optional*|
`name`|`string` *optional*|Name identifier.
`objectPath`|`string` *optional*|Asset path (e.g., /Game/Path/Asset).
`params`|`object` *optional*|Optional action-specific parameters. These are merged with top-level arguments before routing for clients that cannot send arbitrary top-level fields.
`propertyName`|`string` *optional*|Name of the property.
`propertyNames`|`array` *optional*|
`propertyPath`|`string` *optional*|
`snapshotName`|`string` *optional*|
`tag`|`string` *optional*|Name of the tag.
`value`|`string` *optional*|Generic value (any type).

---
#### Tool: **`manage_ai`**
Build AI systems: AI controllers, Behavior Trees, Blackboards, EQS, perception, State Trees, Smart Objects, NavMesh settings, nav modifiers, links, and p

[...]
