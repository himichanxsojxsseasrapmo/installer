while True:
    frame = np.array(screen.grab(detection_box), dtype=np.uint8)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    boxes = model.predict(source=frame, verbose=False, conf=confidence, iou=iou, half=True)
    result = boxes[0]

    if len(result.boxes.xyxy) != 0:
        closest_detection = None
        least_dist = None

        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            relative_head_X = (x1 + x2) // 2
            relative_head_Y = (y1 + y2) // 2 - (y2 - y1) // aim_height

            dist = math.dist((relative_head_X, relative_head_Y), (fov // 2, fov // 2))
            if least_dist is None or dist < least_dist:
                least_dist = dist
                closest_detection = (relative_head_X, relative_head_Y)

        if closest_detection:
            # Calculate offsets
            absolute_head_X = closest_detection[0] + detection_box['left']
            absolute_head_Y = closest_detection[1] + detection_box['top']
            x_offset = absolute_head_X - screen_x
            y_offset = absolute_head_Y - screen_y

            # Optional multiplier if you want speed scaling
            final_x = x_offset * (FNLXSPD * 0.1)
            final_y = y_offset * (FNLYSPD * 0.1)

            # Pack and encrypt
            packed = struct.pack("!ff", final_x, final_y)
            encrypted = fast_encrypt(packed)
            sock.sendto(encrypted, (target_ip, target_port))
