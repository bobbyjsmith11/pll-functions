# curl -d "@json_files/event.json" -X POST https://95zr214h42.execute-api.us-east-2.amazonaws.com/dev
# curl -d "@json_files/pllcalc.json" -X POST https://95zr214h42.execute-api.us-east-2.amazonaws.com/dev/solveForComponents
# curl -d "@json_files/simpll.json" -X POST https://95zr214h42.execute-api.us-east-2.amazonaws.com/dev/simulatePll
# curl -d "@json_files/interp.json" -X POST https://95zr214h42.execute-api.us-east-2.amazonaws.com/dev/callInterpolatePhaseNoise
curl -d "@json_files/simpn.json" -X POST  https://95zr214h42.execute-api.us-east-2.amazonaws.com/dev/callSimulatePhaseNoise
