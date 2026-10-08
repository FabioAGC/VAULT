they rely heavily on vertex color painting, but they also have a lot of full screen gradients and some real time lighting thrown in.

Flat shaded meshes. Careful attention to lighting (few lights, some sun lamps but not all sun lamps). Some meshes (clouds, leaves) look like billboards: planes with constraints to point at the camera. No specular. No ambient on foreground meshes.

I’m 95% sure this game uses zero lighting. There are no dynamic shadows whatsoever, so no need for lights. Meaning that lighting (and probably fog) are part of the texture of the various planes. In other words, to make it look like KRZ, you draw it and color it like KRZ.

I don't know this game at all, but you don't need to have dynamic shadows to have lighting. You can bake textures. Yes, you draw and color it like KRZ. What techniques were used to draw and color it though?

I think it’s all textured planes in 3D space. Also the lighting is very monochromatic

Constant shading on flat planes, with alpha clipped textures most likely made in a vector program like Adobe Illustrator OR single color, constant shaded meshes for each color combined to work like sprites and static scene elements. Pretty sure this is NOT shaded with actual lighting and fog. Instead, all color, shadow, and distance cues built up by a skilled 2d illustrator.