import json
import pll_calcs

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }


    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

    return response

def solveComponents(event, context):
    """
    """
    try:
        d = json.loads(event['body'])
    except:
        body = {
            "message": "Exception!",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response

    fc = float(d['fc'])
    pm = float(d['pm'])
    kphi = float(d['kphi'])
    kvco = float(d['kvco'])
    N = float(d['N'])
    gamma = float(d['gamma'])
    loop_type = d['loop_type']
    comps = pll_calcs.solveForComponents(fc, pm, kphi, kvco, N, gamma, loop_type=loop_type)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(comps)
    }

    return response

def callSimulatePll(event, context):
    """
    """
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    try:
        d = json.loads(event['body'])
    except:
        d = {
            "message": "Exception!",
            "input": event
        }

    fstart = float(d['fstart'])
    fstop = float(d['fstop'])
    ptsPerDec = float(d['ptsPerDec'])
    kphi = float(d['kphi'])
    kvco = float(d['kvco'])
    N = float(d['N'])
    R = float(d['R'])
    flt = {
        'c1': float(d['c1']),
        'c2': float(d['c2']),
        'c3': float(d['c3']),
        'c4': float(d['c4']),
        'r2': float(d['r2']),
        'r3': float(d['r3']),
        'r4': float(d['r4']),
        'flt_type': d['flt_type']
    }

    f, g, p, fz, pz, ref_cl, vco_cl = pll_calcs.simulatePll(fstart, fstop, ptsPerDec, kphi, kvco, N, R, filt=flt)
    d_ret = { 'freqs':f,
              'gains':g,
              'phases':p,
              'fzero': fz,
              'pzero': pz,
              'ref_cl': ref_cl,
              'vco_cl': vco_cl,
            }

    response = {
        "statusCode": 200,
        "body": json.dumps(d_ret)
    }

    return response