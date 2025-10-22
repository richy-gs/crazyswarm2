"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from crazyflie_py import Crazyswarm


TAKEOFF_DURATION = 5.0
HOVER_DURATION = 10.0
LAND_DURATION = 5.0

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    # take off all available crazyflies
    cfs = swarm.allcfs.crazyflies

    for cf in cfs:
        cf.takeoff(targetHeight=2.0, duration=TAKEOFF_DURATION)

    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)

    for cf in cfs:
        cf.land(targetHeight=0.04, duration=LAND_DURATION)

    # timeHelper.sleep(LAND_DURATION)


if __name__ == '__main__':
    main()