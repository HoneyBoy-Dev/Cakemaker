JSON = (loadfile "cakemaker/JSON.lua") -- one-time load of the routines
JSON = require("cakemaker/JSON")
CK = {}
game = {}

function CK.timer()
    local timer = {
        time=0,
        init=true
    }

    function timer.start()
        if timer.init then
            timer.time += 1
        end
    end

    function timer.stop()
        timer.init = false
    end

    function timer.get()
        return timer.time
    end

    return timer
end

function CK.json_load(path)
    archivo = io.open(path, "r")
    tabla = ''
    tabla = archivo:read("*all")
    archivo:close()
    return JSON:decode(tabla)
end

game = CK.json_load("game/default.json")

-- DRAW A BACKGROUND WITH A COLOR
function CK.setBackground(r, g, b)
    screen.clear(color.new(r, g, b))
end

function resources()
    -- LOAD SPRITES
    no_frame = image.load("cakemaker/noneimg.png")
    for i=1, #game["animations"] do
        for frame=1, #game["animations"][i]["frames"] do
            img = image.load(game["animations"][i]["frames"][frame])
            game["animations"][i]["frames"][frame] = (img or no_frame)
        end
    end

    -- LOAD BIHAVIORS
    for j=1, #game["objects"] do
        -- ADD VARS PRIVATE
        game["objects"][j]["time"] = 0
        if #game["objects"][j]["behaviors"] then
            for k=1, #game["objects"][j]["behaviors"] do
                if game["objects"][j]["behaviors"][k] == "obstacle" then
                    game["objects"][j]["face"] = {}
                    break
                end
            end
        end
    end
    
end
resources()

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
            if game["objects"][i]["animation"] ~= name then
                game["objects"][i]["frame"] = 1
                game["objects"][i]["time"] = 0
                game["objects"][i]["animation"] = name
                break
            end
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

camera = {
    x = 0,
    y = 0,
    offx = 480 / 2,
    offy = 272 / 2
}
function CK.update()
    -- RENDER OBJECTS
    for i=1, #game["objects"] do
        -- GET PROPIERTIES
        local name = game["objects"][i]["name"]
        local x = game["objects"][i]["x"]
        local y = game["objects"][i]["y"]
        local w = game["objects"][i]["w"]
        local h = game["objects"][i]["h"]
        local angle = game["objects"][i]["angle"]
        local time = game["objects"][i]["time"]
        local frame = game["objects"][i]["frame"]
        local frame_speed = game["objects"][i]["frame_speed"]
        local animation = game["objects"][i]["animation"]
        local current_animation = 0
        

        -- CURRENT ANIMATION
        for current=1, #game["animations"] do
            if game["animations"][current]["name"] == animation then
                current_animation = current
                break
            end
        end

        -- ANIMATION SYSTEM
        local frames = #game["animations"][current_animation]["frames"]
        if time < 1000 then
            game["objects"][i]["time"] += frame_speed
        else
            game["objects"][i]["time"] = 0
            if frame < frames then
                game["objects"][i]["frame"] += 1
            else
                game["objects"][i]["frame"] = 1
            end
        end

        -- GET BEHAVIOR PLAYER
        local isPlayer = false
        local isCamera = false
        for behavior=1, #game["objects"][i]["behaviors"] do
            if game["objects"][i]["behaviors"][behavior] == "player" then
                isPlayer = true
            end
            if game["objects"][i]["behaviors"][behavior] == "camera" then
                isCamera = true
            end
        end

        -- COLLISION
        if isPlayer then
            -- face collision
            game["objects"][i]["top"] = false
            game["objects"][i]["bottom"] = false
            game["objects"][i]["left"] = false
            game["objects"][i]["right"] = false

            for j=1, #game["objects"] do
                local isObstacle = false
                local name = game["objects"][j]["name"]
                local x2 = game["objects"][j]["x"]
                local y2 = game["objects"][j]["y"]
                local w2 = game["objects"][j]["w"]
                local h2 = game["objects"][j]["h"]
                local inX = false
                local inY = false

                for behavior=1, #game["objects"][j]["behaviors"] do
                    if game["objects"][j]["behaviors"][behavior] == "obstacle" then
                        isObstacle = true
                    end
                end

                if isObstacle then
                    local inX = x + w > x2 and x < x2 + w2
                    local inY = y + h > y2 and y < y2 + h2

                    local playerHalfW = w / 2
                    local playerHalfH = h / 2
                    
                    local obstacleHalfW = w2 / 2
                    local obstacleHalfH = h2 / 2
                    
                    local playerCenterX = x + w / 2
                    local playerCenterY = y + h / 2
                    
                    local obstacleCenterX = x2 + w2 / 2
                    local obstacleCenterY = y2 + h2 / 2

                    -- Calculate the distance between centers
                    local diffX = playerCenterX - obstacleCenterX
                    local diffY = playerCenterY - obstacleCenterY

                    -- Calculate the minimum distance to separate along X and Y
                    local minXDist = playerHalfW + obstacleHalfW
                    local minYDist = playerHalfH + obstacleHalfH

                    local depthX = diffX > 0 and minXDist - diffX or -minXDist - diffX
                    local depthY = diffY > 0 and minYDist - diffY or -minYDist - diffY

                    if inX and inY then
                        if depthX ~= 0 and depthY ~= 0 then
                            if math.abs(depthX) < math.abs(depthY) then
                                if depthX > 0 then
                                    -- left
                                    game["objects"][i]["x"] = x2 + w2
                                    game["objects"][i]["left"] = true
                                else
                                    -- right
                                    game["objects"][i]["x"] = x2 - w
                                    game["objects"][i]["right"] = true
                                end
                            else
                                if depthY > 0 then
                                    -- top
                                    game["objects"][i]["y"] = y2 + h2
                                    game["objects"][i]["top"] = true
                                else
                                    -- bottom
                                    game["objects"][i]["y"] = y2 - h
                                    game["objects"][i]["bottom"] = true
                                end
                            end
                        end
                    end
                end
            end
        end

        -- SHOW OBJECTS
        img = game["animations"][current_animation]["frames"][frame]

        image.resize(
            img,
            w,
            h
        )
        
        image.rotate(
            img,
            angle
        )

        if isCamera then
            camera.x = x - camera.offx
            camera.y = y - camera.offy
        end

        image.blit(
            img,
            x - camera.x,
            y - camera.y
        )

    end
end


