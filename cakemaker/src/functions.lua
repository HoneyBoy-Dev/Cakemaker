function CK.get(name, propiertie)
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == name then
            result = game["objects"][i][propiertie]
            break
        end
    end
    return result
end

function CK.set(name, propiertie, value)
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == name then
            game["objects"][i][propiertie] = value
            break
        end
    end
end

function CK.set_animation(obj, name)
    -- GET OBJECTS
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == obj then
            --game["objects"][i]["time"] = 0
            --game["objects"][i]["frame"] = 1
            game["objects"][i]["animation"] = name
            break
        end
    end
end

function CK.set_rotate(obj, angle)
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == obj then
            game["objects"][i]["angle"] = angle
            break
        end
    end    
end

function CK.set_rotation(obj, angle)
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == obj then
            game["objects"][i]["angle"] += angle
            break
        end

        if game["objects"][i]["angle"] > 360 then
            game["objects"][i]["angle"] = 0
        end
    end    
end

-- COLLISION DETECTION
function CK.get_collision(obj)
    obj_index = 1
    obj_name = ""
    is_collision = false

    -- GET POS OF OBJ
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == obj then
            obj_index = i
            obj_name = game["objects"][i]["name"]
            break
        end
    end

    -- FIRST OBJ
    obj_x = game["objects"][obj_index]["x"]
    obj_y = game["objects"][obj_index]["y"]
    obj_w = game["objects"][obj_index]["w"]
    obj_h = game["objects"][obj_index]["h"]

    for i=1, #game["objects"] do
        is_x = false
        is_y = false
        -- SECOND OBJ
        obj2_name = game["objects"][i]["name"]
        obj2_x = game["objects"][i]["x"]
        obj2_y = game["objects"][i]["y"]
        obj2_w = game["objects"][i]["w"]
        obj2_h = game["objects"][i]["h"]
        -- COMPARE NAME
        if obj_name ~= obj2_name then
            -- X
            if obj_x + obj_w > obj2_x then
                if  obj_x < obj2_x + obj2_w then 
                    is_x = true
                end
            end
            -- Y
            if obj_y + obj_h > obj2_y then
                if obj_y < obj2_y + obj2_h then
                    is_y = true
                end
            end
        end

        is_collision = false
        if is_x and is_y then
            is_collision = true
            break
        end
    end

    return is_collision
end

function CK.get_collision_between(obj, obj2)
    local obj1_i = 0
    local obj2_i = 0
    local is_collision = false

    -- GET POS OF OBJ1
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == obj then
            obj1_i = i
            break
        end
    end
    -- GET POS OF OBJ2
    for i=1, #game["objects"] do
        if game["objects"][i]["name"] == obj2 then
            obj2_i = i
            break
        end
    end

    obj1_x = game["objects"][obj1_i]["x"]
    obj1_y = game["objects"][obj1_i]["y"]
    obj1_w = game["objects"][obj1_i]["w"]
    obj1_h = game["objects"][obj1_i]["h"]

    obj2_x = game["objects"][obj2_i]["x"]
    obj2_y = game["objects"][obj2_i]["y"]
    obj2_w = game["objects"][obj2_i]["w"]
    obj2_h = game["objects"][obj2_i]["h"]

    if obj1_x + obj1_w > obj2_x and  obj1_x < obj2_x + obj2_w then
        if obj1_y + obj1_h > obj2_y and  obj1_y < obj2_y + obj2_h then
            is_collision = true
        end
    end

    return is_collision
end