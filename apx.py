while True:
    start_time = time.perf_counter()
    initial_frame = screen.grab(detection_box)
    frame = np.array(initial_frame, dtype=np.uint8)
    
    if frame is None or frame.size == 0:
        continue
        
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    boxes = model.predict(source=frame, verbose=False, conf=conf, iou=iou, half=True)
    result = boxes[0]
    
    if len(result.boxes.xyxy) != 0: #player detected
        least_crosshair_dist = closest_detection = player_in_frame = False
        
        for box in result.boxes.xyxy: #iterate over each player detected
            x1, y1, x2, y2 = map(int, box)
            x1y1 = (x1, y1)
            x2y2 = (x2, y2)
            height = y2 - y1
            relative_head_X, relative_head_Y = int((x1 + x2)/2), int((y1 + y2)/2 - height/aim_height)
            own_player = x1 < 15 or (x1 < box_constant/5 and y2 > box_constant/1.2)

            #calculate the distance between each detection and the crosshair
            crosshair_dist = math.dist((relative_head_X, relative_head_Y), (box_constant/2, box_constant/2))

            if not least_crosshair_dist: 
                least_crosshair_dist = crosshair_dist

            if crosshair_dist <= least_crosshair_dist and not own_player:
                least_crosshair_dist = crosshair_dist
                closest_detection = {"x1y1": x1y1, "x2y2": x2y2, "relative_head_X": relative_head_X, "relative_head_Y": relative_head_Y}

            if own_player:
                own_player = False
                if not player_in_frame:
                    player_in_frame = True

        if closest_detection: #if valid detection exists
            cv2.circle(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), 5, (115, 244, 113), -1)
            cv2.line(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), (box_constant//2, box_constant//2), (244, 242, 113), 2)

            absolute_head_X, absolute_head_Y = closest_detection["relative_head_X"] + detection_box['left'], closest_detection["relative_head_Y"] + detection_box['top'] #finalcoordinates
            x1, y1 = closest_detection["x1y1"]
            threshold = 5
            is_locked = screen_x - threshold <= absolute_head_X <= screen_x + threshold and screen_y - threshold <= absolute_head_Y <= screen_y + threshold

            if is_locked:
                # Check if trigger bot should shoot
                if use_trigger_bot and aimbot_status == colored("ENABLED", 'green'):
                    is_shooting = win32api.GetKeyState(0x01) in (-127, -128)
                    if not is_shooting:
                        # Trigger shot (left click)
                        ctypes.windll.user32.mouse_event(0x0002) #left mouse down
                        time.sleep(0.0001)
                        ctypes.windll.user32.mouse_event(0x0004) #left mouse up

                cv2.putText(frame, "LOCKED", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (115, 244, 113), 2)
            else:
                cv2.putText(frame, "TARGETING", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (115, 113, 244), 2)
            movement_x = absolute_head_X - screen_x
            movement_y = absolute_head_Y - screen_y
            #mousemove(movement_x,movement_y)
