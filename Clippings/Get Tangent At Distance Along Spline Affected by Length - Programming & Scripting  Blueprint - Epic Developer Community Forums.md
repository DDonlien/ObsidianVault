---
title: "Get Tangent At Distance Along Spline Affected by Length - Programming & Scripting / Blueprint - Epic Developer Community Forums"
source: "https://forums.unrealengine.com/t/get-tangent-at-distance-along-spline-affected-by-length/433861"
author:
  - "[[anonymous_user_705e34d1]]"
published: 2018-09-16
created: 2025-02-18
description: "I’m using a Spline Component to create a road network. In order to keep the road pieces from stretching/squashing, I’ve used “GetTangentAtDistanceAlongSpline” to get the start/end tangents of each piece. However when I&hellip;"
tags:
  - "clippings"
---
I’m using a Spline Component to create a road network.

In order to keep the road pieces from stretching/squashing, I’ve used “GetTangentAtDistanceAlongSpline” to get the start/end tangents of each piece.

However when I move the points of the spline too far apart, the tangents become distorted.  
The distortion happens when the distance between two spline points is greater than the length of one length of road.

![253809-splinepoints.png](https://d3kjluh73b9h9o.cloudfront.net/original/4X/9/5/c/95c3476ca1300642d41c7a73d837039fc3c47a12.png)

When the distance between two points is less than one length, the tangent seems to have less of an effect on any spline mesh created with it.

![253810-lessthanonelength.png](https://d3kjluh73b9h9o.cloudfront.net/original/4X/8/f/e/8fe5d8350180d9b207b78f4c0e0da16a38efe10c.png)

Found a workaround.

It seems the length of the tangent is increased as the distance between points increases.  
(I’m not sure if this is intended behaviour)

Basically I just normalized the tangent vector and multiply it by the length of one road unit.

![253813-fix.png](https://d3kjluh73b9h9o.cloudfront.net/original/4X/7/b/0/7b0f94717b0c653ccd2c6943068b33178fe65cd5.png)

Thank you!! You just saved me hours of guess work and debugging! ![:heart:](https://d1ap1mz92jnks1.cloudfront.net/images/emoji/twitter/heart.png?v=12 ":heart:")

thanks man, that helped me too!

You have saved me a lot of head ache! thanks!

Years later and this is still helpful, thanks!