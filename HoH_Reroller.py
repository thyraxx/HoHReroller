import pyautogui

rerollImage = pyautogui.locateOnScreen('reroll_hundred.png', region=(840, 733, 230, 30));
rerollImageLight = pyautogui.locateOnScreen('reroll_hundred_light.png', region=(840, 733, 230, 30));
rerollImageClicked = pyautogui.locateOnScreen('reroll_hundred_clicked.png', region=(840, 733, 230, 30));
print(rerollImage);

count = 0;

def click():
	pyautogui.mouseDown(); 
	pyautogui.mouseUp();

while True:
	count += 1
	itemImage = pyautogui.locateOnScreen('oldmap.png', region=(687, 466, 45, 290));
	#itemImage2 = pyautogui.locateOnScreen('heartseeker.png', region=(687, 466, 45, 290));
	if str(itemImage) != 'None':
		print("Item Found!");
		itemImageX = itemImage.left;
		itemImageY = itemImage.top;
		pyautogui.moveTo(itemImageX+50, itemImageY);
		click();
		break;
	else:
		pyautogui.moveTo(850, 750);
		if str(rerollImage) != 'None' or str(rerollImageLight) !='None' or str(rerollImageClicked) !='None':
			click();
		# else:
		# 	if str(rerollImageLight !='None'):
		# 		click();
		# 	else:
		# 		if str(rerollImageClicked) !='None':	
		# 			click();

	if count == 100:
		break;


#item list coords 
#start 687, 466
#end 739, 738

#reroll coords
#840, 733
#1070, 760