"""Translation-independent obstruction to the printed00-forced-by22 claim."""


def normalized(points):
    a=min(x for x,y in points);b=min(y for x,y in points)
    return tuple(sorted((x-a,y-b) for x,y in points))


def verify():
    base={(0,0),(1,0),(2,0),(3,0),(1,1)};orientations=set()
    for reflect in [False,True]:
        points={(x,-y if reflect else y) for x,y in base}
        for _ in range(4):
            orientations.add(normalized(points));points={(y,-x) for x,y in points}
    assert len(orientations)==8
    report=[]
    for points in sorted(orientations):
        spans=(max(x for x,y in points)+1,max(y for x,y in points)+1)
        assert spans in [(2,4),(4,2)]
        differences={(x-u,y-v) for x,y in points for u,v in points}
        assert (2,2) not in differences and (-2,-2) not in differences
        report.append(dict(cells=points,spans=spans,contains_diagonal_difference_22=False))
    return dict(orientations=report,claim='No translation or orientation of Y can contain both00 and22.',
                reason='Those two cells require a3x3 bounding box; everyY has one dimension2.',
                implication='A nonempty primary22 column cannot force00 under AlgorithmP; shortening never adds cells.')


if __name__=='__main__':
    import json
    print(json.dumps(verify(),indent=2))
