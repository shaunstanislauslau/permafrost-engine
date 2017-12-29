#include "public/render.h"
#include "shader.h"
#include "texture.h"

bool R_Init(const char *base_path)
{
    R_Texture_Init();

    return Shader_InitAll(base_path);    
}
