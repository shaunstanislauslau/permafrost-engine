/*
 *  This file is part of Permafrost Engine. 
 *  Copyright (C) 2018 Eduard Permyakov 
 *
 *  Permafrost Engine is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  Permafrost Engine is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 *  Linking this software statically or dynamically with other modules is making 
 *  a combined work based on this software. Thus, the terms and conditions of 
 *  the GNU General Public License cover the whole combination. 
 *  
 *  As a special exception, the copyright holders of Permafrost Engine give 
 *  you permission to link Permafrost Engine with independent modules to produce 
 *  an executable, regardless of the license terms of these independent 
 *  modules, and to copy and distribute the resulting executable under 
 *  terms of your choice, provided that you also meet, for each linked 
 *  independent module, the terms and conditions of the license of that 
 *  module. An independent module is a module which is not derived from 
 *  or based on Permafrost Engine. If you modify Permafrost Engine, you may 
 *  extend this exception to your version of Permafrost Engine, but you are not 
 *  obliged to do so. If you do not wish to do so, delete this exception 
 *  statement from your version.
 *
 */

#ifndef SCENE_H
#define SCENE_H

#include "pf_math.h"
#include "lib/public/kvec.h"
#ifndef __USE_POSIX
    #define __USE_POSIX /* strtok_r */
#endif
#include "lib/public/khash.h"

#include <stdbool.h>

struct attr{
    char key[64];
    enum{
        TYPE_STRING,
        TYPE_FLOAT,
        TYPE_INT,
        TYPE_VEC3,
        TYPE_QUAT,
        TYPE_BOOL,
    }type;
    union{
        char   as_string[64];
        float  as_float;
        int    as_int;
        vec3_t as_vec3;
        quat_t as_quat;
        bool   as_bool;
    }val;
};

KHASH_DECLARE(attr, kh_cstr_t, struct attr)
typedef kvec_t(struct attr) kvec_attr_t;

bool Scene_Load(const char *path);

#endif

