
; This patch contains fixes to various bugs present in vanilla Wind Waker.


; If the player heals grandma but doesn't have an empty bottle for her to put soup in because they swapped their equipped item out too fast, grandma will crash the game because she tries to say a message that doesn't exist in the game's script.
; Change grandma to say the same message regardless of whether you have an empty bottle or not.
.open "files/rels/d_a_npc_ba1.rel" ; Grandma
.org 0x16DC
  ; This line originally hardcoded message ID 2041, which would be the message grandma says when you heal her without an empty bottle.
  ; Change it to 2037, which is the normal message ID when you do have an empty bottle.
  li r0, 2037
.close




; Fix a crash when you look at the broken shards of Helmaroc King's mask with the hookshot.
.open "sys/main.dol"
.org 0x800F13A8 ; In daHookshot_rockLineCallback
  b hookshot_sight_failsafe_check
; Part of the code for the hookshot's sight expects entities you look at to have a pointer in a specific place.
; The broken shards of Helmaroc King's mask don't have that pointer so looking at them with hookshot crashes.
.org @NextFreeSpace
.global hookshot_sight_failsafe_check
hookshot_sight_failsafe_check:
  cmplwi r30, 0
  beq hookshot_sight_failsafe
  b hookshot_sight_return
  
  ; If r30 is null skip to the code that hides the hookshot sight.
  hookshot_sight_failsafe:
  b 0x800F13C0
  
  ; Otherwise we replace the line of code at 800F13A8 we replaced to jump here, then jump back.
  hookshot_sight_return:
  lwz r0, 0x01C4 (r30)
  b 0x800F13AC
.close




; If you try to challenge Orca when you have no sword equipped, the game will crash.
; This is because he tries to create the counter in the lower left corner of the screen for how many hits you've gotten, but that counter needs a sword icon, and the sword icon texture is not loaded in when you have no sword equipped.
; So change it so he doesn't create a counter at all when you have no sword.
.open "files/rels/d_a_npc_ji1.rel" ; Orca
.org 0xC914
  cmpwi r0, 0x38 ; Hero's Sword
  beq 0xC938 ; Use Hero's Sword icon for the counter (icon 1)
  cmpwi r0, 0xFF ; No sword
  beq 0xC96C ; Skip past the code to create the counter entirely
  b 0xC948 ; Use Master Sword icon for the counter (icon 2)
.close




; Don't allow Beedle to buy Blue Chu Jelly, as selling that can make getting the Blue Potion from Doc Bandam impossible.
.open "files/rels/d_a_npc_bs1.rel" ; Beedle
.org 0x214C
  b 0x21DC ; Make Beedle not consider Blue Chu Jelly to be a spoil
.close




; Auto-equip the Deluxe Picto Box when obtaining it.
.open "sys/main.dol"
.org 0x800C3420 ; In item_func_camera2__Fv (Deluxe Picto Box item get func)
  b deluxe_picto_box_item_func_fix_equipped_picto_box

; In vanilla, the Deluxe Picto Box item get func doesn't update the Picto Box equipped on the X/Y/Z button.
; This causes it to not work correctly until the equipped item is fixed (by reloading the area or manually re-equipping it).
; This custom code adds a check to fix it automatically into the item get func.
.org @NextFreeSpace
.global deluxe_picto_box_item_func_fix_equipped_picto_box
deluxe_picto_box_item_func_fix_equipped_picto_box:
  stb r0, 0x44 (r3) ; Replace the line of code we overwrote to jump heree
  
  li r4, 0 ; The offset for which button to check next (0/1/2 for X/Y/Z)
  li r0, 3 ; How many times to loop (3 buttons)
  mtctr r0
  
  deluxe_picto_box_item_func_fix_equipped_picto_box_loop_start:
  add r5, r3, r4 ; Add the current button offset for this loop to the pointer
  lbz r0, 0x5BD3 (r5) ; Read the item ID on the current button
  ; (Note: r3 starts with 803C4C08 in it, so offset 5BD3 is used to get the list of items on the X/Y/Z buttons, at 803CA7DB.)
  cmplwi r0, 0x23 ; Normal Picto Box ID
  ; If this button doesn't have the normal Picto Box equipped, continue the loop.
  bne deluxe_picto_box_item_func_fix_equipped_picto_box_continue_loop
  
  ; If this button does have the normal Picto Box equipped, replace it with the Deluxe Picto Box.
  li r0, 0x26 ; Deluxe Picto Box ID
  stb r0, 0x5BD3 (r5)
  
  deluxe_picto_box_item_func_fix_equipped_picto_box_continue_loop:
  addi r4, r4, 1
  bdnz deluxe_picto_box_item_func_fix_equipped_picto_box_loop_start
  
  b 0x800C3424 ; Return
.close




; Delete Morths that fall out-of-bounds.
.open "files/rels/d_a_ks.rel" ; Morth
.org 0x678 ; In naraku_check__FP8ks_class
  ; This function was originally intended to delete Morths that fall into pits that cause Link to void out.
  ; We tweak it so that, instead of ignoring when the Morth has no collision below it, it runs the same deletion code in that case as when it has void-out-collision under it.
  beq 0x6b0
.close




; Fix a vanilla bug where cutting Stalfos in half and then hitting the upper body with light arrows would make the lower body permanently unkillable.
.open "files/rels/d_a_st.rel" ; Stalfos
.org 0x85CC
  bl stalfos_kill_lower_body_when_upper_body_light_arrowed

; Fix the lower body of a Stalfos not dying when the upper body dies to light arrows.
.org @NextFreeSpace
.global stalfos_kill_lower_body_when_upper_body_light_arrowed
stalfos_kill_lower_body_when_upper_body_light_arrowed:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)
  
  bl fopAcIt_Judge__FPFPvPv_PvPv ; Get upper body entity
  cmplwi r3, 0
  beq stalfos_kill_lower_body_when_upper_body_light_arrowed_end
  
  lbz r0, 0x1FAE (r3) ; Counter for how many frames the upper body has been dying to light arrows
  cmpwi r0, 0
  beq stalfos_kill_lower_body_when_upper_body_light_arrowed_end ; The upper body hasn't been hit with light arrows, so don't kill the lower body either
  
  lbz r0, 0x1FAE (r31) ; Counter for how many frames the lower body has been dying to light arrows
  cmpwi r0, 0
  bne stalfos_kill_lower_body_when_upper_body_light_arrowed_end ; The lower body is already dying to light arrows, so don't reset its counter
  
  li r0, 1
  stb r0, 0x1FAE (r31) ; Start the lower body's counter for dying to light arrows at 1
  
  stalfos_kill_lower_body_when_upper_body_light_arrowed_end:
  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr
.close




; Fix a vanilla bug where Miniblins killed with light arrows will not set their death switch.
; (Note: This fix still does not fix the case where the Miniblin is supposed to set switch index 0 on death, but there are no Miniblins in the game that are supposed to set that, so it doesn't matter.)
.open "files/rels/d_a_pt.rel" ; Miniblin
.org 0x4B44
  bl miniblin_set_death_switch_when_light_arrowed

; Fix Miniblins not setting a switch on death if killed with Light Arrows.
.org @NextFreeSpace
.global miniblin_set_death_switch_when_light_arrowed
miniblin_set_death_switch_when_light_arrowed:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)
  
  bl Set__8dCcD_SphFRC11dCcD_SrcSph ; Replace the function call we overwrote to call this custom function
  
  lbz r0, 0x2B4 (r29) ; Read the behavior type param for the Miniblin
  cmpwi r0, 0 ; Behavior type 0 is a respawning Miniblin
  beq miniblin_set_death_switch_when_light_arrowed_end ; Respawning Miniblins should not set a switch when they die, so don't do anything
  
  ; Otherwise it's a single Miniblin, so it should set a switch when it dies.
  lbz r0, 0x2B8 (r29) ; Read the switch index param the non-respawning Miniblin should set on death
  stb r0, 0x995 (r29) ; Store it into the Miniblin's enemyice struct as the switch index it should set when it dies to Light Arrows.
  ; Note: The enemy_ice function does not set the switch specified here in the case that it's switch index 0, but the Miniblin itself would even for index 0. This doesn't matter in practice because no Miniblins placed in the game are supposed to set switch index 0 on death.
  
  miniblin_set_death_switch_when_light_arrowed_end:
  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr
.close




; Fix a vanilla bug where Jalhalla's child Poes would not tell Jalhalla they died when hit by light arrows.
.open "files/rels/d_a_pw.rel" ; Poe
.org 0x8CC
  ; Remove a check that the Poe's HP must be <= 0 for it to be considered dead by Jalhalla.
  ; We're going to add this back in our custom code, we just need to remove it here so the original code reaches the function call we hijack to insert custom code, so that we can have it check (HP <= 0 || isDyingToLightArrows).
  b 0x8D8
.org 0x900
  bl poe_fix_light_arrows_bug
; Fix child Poes not telling Jalhalla they died when hit with light arrows.
.org @NextFreeSpace
.global poe_fix_light_arrows_bug
poe_fix_light_arrows_bug:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)
  
  lbz r0, 0x285 (r31) ; Read the Poe's current HP
  extsb. r0,r0
  ble poe_fix_light_arrows_bug_poe_is_dead ; Consider the Poe dead if its HP is <= 0
  
  lbz r0, 0x88A (r31) ; Read the Poe's dying to light arrows counter
  cmpwi r0, 0
  bgt poe_fix_light_arrows_bug_poe_is_dead ; Consider the Poe dead if it was hit with light arrows, even if its HP isn't 0 yet
  
  b poe_fix_light_arrows_bug_return_false ; Otherwise consider the Poe alive
  
  poe_fix_light_arrows_bug_poe_is_dead:
  bl fopAcM_SearchByID__FUiPP10fopAc_ac_c ; Replace the function call we overwrote to call this custom function
  
  ; Then we need to reproduce most of the rest of the original Big_pow_down_check function.
  ; The reason for this is a weird quirk Poes in the Jalhalla fight have where if they're killed in the last 4 frames before Jalhalla reforms, they will "unkill" themselves so they can join back up with Jalhalla.
  ; We need to unset the dying to light arrows counter in that case as well.
  
  cmpwi r3, 0
  beq poe_fix_light_arrows_bug_return_false
  lwz r4, 0x18 (sp) ; Read Jalhalla entity pointer (original code used sp+8 but this function's stack offset is +0x10)
  cmplwi r4, 0
  beq poe_fix_light_arrows_bug_return_false
  lha r0, 8 (r4)
  cmpwi r0, 0xD4 ; Check to be sure the supposed Jalhalla entity is actually an instance of bpw_class.
  bne poe_fix_light_arrows_bug_return_false
  lha r0, 0x446 (r4)
  cmpwi r0, 0x6F ; Check Jalhalla's state or something, 0x6F is for when the child Poes are running around
  bne poe_fix_light_arrows_bug_unkill_poe
  lha r0, 0x44E (r4) ; Read number of frames left until Jalhalla reforms
  cmpwi r0, 3 ; Poes killed within the last 4 frames before Jalhalla reforms shouldn't actually die
  ble poe_fix_light_arrows_bug_unkill_poe
  lbz r3, 0x285 (r4)
  addi r0, r3, -1 ; Decrement Jalhalla's HP
  stb r0, 0x285 (r4)
  lwz r3, 0x18 (sp) ; Read Jalhalla entity pointer again
  lbz r0, 0x285 (r3) ; Check if Jalhalla's HP is zero, meaning this Poe that just died was the last one
  extsb. r0,r0
  bgt poe_fix_light_arrows_bug_not_the_last_poe
  li r0, 1
  stb r0, 0x344 (r31)
  poe_fix_light_arrows_bug_not_the_last_poe:
  li r0, 1
  stb r0, 0x345 (r31)
  b poe_fix_light_arrows_bug_return_false
  
  poe_fix_light_arrows_bug_unkill_poe:
  li r0,4
  stb r0, 0x285 (r31)
  
  ; These 2 lines are the new code:
  li r0, 0
  stb r0, 0x88A (r31) ; Set the Poe's dying to light arrows counter to zero to stop it from dying
  
  li r3, 1
  b poe_fix_light_arrows_bug_end
  
  poe_fix_light_arrows_bug_return_false:
  li r3, 0
  
  poe_fix_light_arrows_bug_end:
  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr
.org 0x904
  ; Our custom function replaces the entire rest of this function, so just return after the custom function finished.
  lwz r31, 0x1C (r1)
  lwz r0, 0x24 (r1)
  mtlr r0
  addi r1, r1, 0x20
  blr
.close




; Fix a vanilla bug where respawning Magtails would not respawn if you shoot their head with Light Arrows.
.open "files/rels/d_a_mt.rel" ; Magtail
.org 0x6000
  bl magtail_respawn_when_head_light_arrowed
.org @NextFreeSpace
.global magtail_respawn_when_head_light_arrowed
magtail_respawn_when_head_light_arrowed:
  stwu sp, -0x10 (sp)
  mflr r0
  stw r0, 0x14 (sp)
  
  bl GetTgHitObj__12dCcD_GObjInfFv ; Replace the function call we overwrote to call this custom function
  
  ; Then we need to reproduce a few lines of code from the original function.
  stw r3, 0x40 (sp) ; Write the TgHitObj (original code used sp+0x30 but this function's stack offset is +0x10)
  addi r0, r30, 0x1874
  stw r0, 0x54 (sp) ; Write something from the Magtail entity (original code used sp+0x44 but this function's stack offset is +0x10)
  lwz r0, 0x10 (r3) ; Read the bitfield of damage types done by the actor that just damaged this Magtail
  rlwinm. r0, r0, 0, 11, 11 ; Check the Light Arrows damage type
  
  ; Then if the Light Arrows bit was set, we store true to magtail_entity+0x1CBC to signify that the Magtail should respawn.
  ; (We can't use the original branch on the Light Arrows bit because it's inside the REL.)
  beq magtail_respawn_when_head_light_arrowed_end
  li r0, 1
  stb r0, 0x1CBC (r30)
  
  magtail_respawn_when_head_light_arrowed_end:
  lwz r0, 0x14 (sp)
  mtlr r0
  addi sp, sp, 0x10
  blr
.org 0x6004
  ; Then remove some lines of code after the function call we had to move into the custom function.
  nop
  nop
  nop
  nop
  nop
.close




; Fixes Phantom Ganon 1's hardcoded fight trigger region in FF2 to check Link's Y position.
; This is so it doesn't trigger when the player is much higher than Phantom Ganon, and is trying to go fight Helmaroc.
.open "files/rels/d_a_fganon.rel"
.org 0x4F50
  b phantom_ganon_check_link_within_y_diff

.org @NextFreeSpace
.global phantom_ganon_check_link_within_y_diff
phantom_ganon_check_link_within_y_diff:
  lfs f4, 0x1C (sp) ; Read the Y difference between Link and Phantom Ganon
  lfs f3, 0x88 (r31) ; Read the float constant 1000.0 from 0xA918
  
  ; If the Link is 1000.0 units or more higher than PG, do not trigger the fight.
  ; (Does not account for negative difference. Still extends infinitely downwards.)
  fcmpo cr0, f4, f3
  bge phantom_ganon_check_link_within_y_diff_outside_range
  
  ; Otherwise, go on to check the X and Z difference as usual.
  fmuls f1, f1, f1 ; Replace the line of code we overwrote to jump here
  b 0x4F54

phantom_ganon_check_link_within_y_diff_outside_range:
  b 0x5204
.close




; Reduce Game heap memory fragmentation on the sea by giving a maximum memory estimate for island LoD models.
.open "files/rels/d_a_lod_bg.rel" ; Background island LoD model actor
.org 0xDCC
  ;li r5, 0x4B0 ; For most islands
  ;li r5, 0x970 ; Forsaken Fortress (before it's destroyed - afterwards it uses 0x4B0)
  li r5, 0xEF0 ; Windfall
; Fix useless warnings in the console caused by trying to call JKRHeap::free on a solid heap
.org 0x478
  nop
.org 0x4D0
  nop
.close




; Stop sub BGM (used for miniboss music, as well as item get jingles) when unloading a stage.
; This is to stop the Mothula and Stalfos miniboss music from continuing to play even after leaving their rooms.
; It also stops the Outset whirlpool's music from playing after you lose to it.
.open "sys/main.dol"
.org 0x80235340 ; In dScnPly_Delete(dScnPly_ply_c *)
  b stop_sub_bgm_when_unloading_stage

.org @NextFreeSpace
.global stop_sub_bgm_when_unloading_stage
stop_sub_bgm_when_unloading_stage:
  ; Stop the music.
  lis r3, 0x803F7710@ha
  addi r3, r3, 0x803F7710@l
  lwz r3, 0 (r3)
  bl subBgmStop__11JAIZelBasicFv
  
  ; Replace the line we overwrote to jump here
  mr r3, r30
  
  ; Return
  b 0x80235344
.close




; Zero out the arrow actor's on-hit callback function when it enters the stopped state.
; This is to fix a vanilla crash that could happen if the arrow hit two different actors at the same time.
; The arrow actor keeps track of both the proc ID of the actor it hit and which joint index within that actor it hit.
; The joint index variable is only updated while the arrow is moving, while the proc ID is updated by the callback function.
; If the arrow hit something with more joints first (e.g. Big Octo) and then something with fewer joints (e.g. Big Octo eye), the joint index could wind up higher than the size of the joints array for the second actor.
; So when the actor tries to stop on that joint, it would wind up copying invalid joint data as matrix data.
; Invalid data can sometimes be NaN floats, and storing those as the arrow actor's position would cause an assertion error as positions are supposed to be valid numbers.
; Zeroing out the on-hit callback fixes the crash as the proc ID will no longer be desynced from the joint index.
.open "sys/main.dol"
.org 0x800D6194 ; In daArrow_c::procMove(void)
  b zero_out_arrow_on_hit_callback
.org @NextFreeSpace
.global zero_out_arrow_on_hit_callback
zero_out_arrow_on_hit_callback:
  ; Store 0 to the arrow actor's on-hit callback (atHit_CB).
  ; Specifically this is the dCcD_GObjAt.mpCallback field of the arrow's hitbox.
  li r0, 0
  stw r0, 0x3F4 (r31)
  
  ; Replace the line we overwrote to jump here (preparing to update the arrow's state to 2, stopped).
  li r0, 2
  
  ; Return
  b 0x800D6198
.close




; Do not cancel the currently playing BGM when playing the sun rising tune at 5:59AM (sea_dawn.bms).
; This is to fix a vanilla bug where if you are fighting a Big Octo when the sun rises, the sea 
; miniboss music will be interrupted and replaced by the regular sea enemy music.
; In theory this change shouldn't cause any issues, since a similar function, processMorningToNormal,
; which handles changing the sun rising tune to the regular sea BGM shortly afterwards, already
; calls bgmStart in this way without interrupting the previous BGM.
.open "sys/main.dol"
.org 0x802ABEF8 ; In JAIZelBasic::processTime(void)
  li r6, 1 ; Argument r6 to bgmStart seems to prevent stopping the existing BGM, if one is playing.
.close




; Do not prevent the player from defending with the Skull Hammer when they don't own a shield.
; Originally, the game only checked if you own a shield to know if it should allow you to defend.
; Change it to allow defending if you own a shield, or are holding the Skull Hammer in your hands.
.open "sys/main.dol"
.org 0x8010E288 ; In daPy_lk_c::checkNextActionFromButton(void)
  mr r3, r31 ; Player instance (daPy_lk_c)
  bl check_can_defend
  cmpwi r3, 0
  nop

.org 0x8010E504 ; In daPy_lk_c::setShieldGuard(void)
  mr r3, r31 ; Player instance (daPy_lk_c)
  bl check_can_defend
  cmpwi r3, 0
  nop

.org @NextFreeSpace
; Argument r3 - pointer to the current daPy_lk_c Link player instance
.global check_can_defend
check_can_defend:
  lhz r0, 0x3560 (r3) ; What item the player is holding in their hand
  cmplwi r0, 0x33 # Skull Hammer
  beq check_can_defend_return_true ; Always allow defending if holding the Skull Hammer
  
  lis r3, g_dComIfG_gameInfo@ha
  addi r3, r3, g_dComIfG_gameInfo@l
  lbz r0, 0xF (r3) ; Currently equipped shield ID
  cmplwi r0, 0xFF ; No shield equipped
  bne check_can_defend_return_true ; Also allow defending if you own a shield
  
  ; Otherwise, don't allow defending.
  check_can_defend_return_false:
  li r3, 0
  blr
  
  check_can_defend_return_true:
  li r3, 1
  blr
.close




; During the Ganondorf fight, it is actually possible to reflect Zelda's light arrows during the
; first phase of the fight. This rarely happens as Zelda aims upwards at Ganondorf and not at Link,
; but it is possible.
; But when it does happen, if you are locked on to Ganondorf, and Ganondorf tries to enter the
; second phase of the fight (knocking Zelda out) at the same time as as being hit with the reflected
; arrow, this can cause a bug because of conflicting events.
; Ganondorf starts the short hardcoded camera event to emphasize the fact that you reflected an
; arrow at him at around the same time as the event for knocking Zelda out, which can result in a
; bug where Zelda and Link will not be animated during that event.
; To fix this, we disable that short hardcoded event until Ganondorf has <= 25 HP (phase 3).
; (Bug figured out and fix suggested by SuperDude88.)
.open "sys/main.dol" ; In daArrow_c::ShieldReflect(void)
.org 0x800D4EBC
  ; This code gets run when reflecting a light arrow while locked on to Ganondorf.
  b check_ganondorf_in_phase_3

.org @NextFreeSpace
.global check_ganondorf_in_phase_3
check_ganondorf_in_phase_3:
  lbz r0, 0x285 (r3) ; Ganondorf's current HP
  extsb r0, r0
  cmpwi r0, 25 ; Zelda wakes up and Ganondorf enters phase 3 at 25 HP
  bgt ganondorf_not_in_phase_3

ganondorf_in_phase_3:
  ; Replace the line we overwrote to jump here.
  lfs f0, 0x1F8 (r4)
  ; Return to the original code for reflecting Zelda's light arrow.
  b 0x800D4EC0

ganondorf_not_in_phase_3:
  ; Return to the code ran when you are not locked on to Ganondorf.
  ; This stops Ganondorf from playing the hardcoded camera event if he isn't in phase 3 yet.
  ; We still allow the arrow to be reflected and damage Ganondorf; only the event is removed.
  b 0x800D4F68
.close




; During the Helmaroc King fight, HK could sometimes become stuck on the level geometry while trying
; to land. This is only known to happen after doing the speedrun strat of jumping back into the
; tower while it's closing, as HK only starting using the landing state after the tower closes, and
; there doesn't seem to be any geometry he can get stuck on when you're on top of the tower.
; To fix this, we add a custom timer that counts the number of frames his current landing attempt
; has taken, and when it exceeds a set limit, we switch his state back to the flying upwards state,
; which causes him to break free, fly back to the top, and then try to land again from scratch.
.open "files/rels/d_a_bdk.rel" ; Helmaroc King
.org 0x24D4 ; At the start of HK's landing state's first substate, in landing(bdk_class *)
  b initialize_helmaroc_king_landing_timer
.org 0x2AD0 ; At the end of HK's landing state function, landing(bdk_class *)
  b check_helmaroc_king_landing_timeout
.org @NextFreeSpace
.global initialize_helmaroc_king_landing_timer
initialize_helmaroc_king_landing_timer:
  ; Branch taken for substate 0.
  ; Initialize a timer in the upper two bytes of HK's params field, which were unused in vanilla.
  li r3, 0
  sth r3, 0xB0 (r30) ; Store the initial timer value.
  mr r3, r30 ; Replace the line we overwrote to jump here
  b 0x24D8 ; Return to the landing state's first substate code
.global check_helmaroc_king_landing_timeout
check_helmaroc_king_landing_timeout:
  ; Branch taken for all substates, so we have to check if the substate is 1 or 2, which are the
  ; states he is known to become stuck in. If it is, we increment the timer once per frame, and give
  ; up on the landing if necessary.
  ; Otherwise, for states 3 or 4 or anything else, HK has likely already successfully reached his
  ; landing spot, and is just finishing up the landing. We don't want to make him give up after
  ; succeeding, so just return from the function in that case.
  lha r3, 0x2C8 (r30) ; Load HK's landing substate
  cmpwi r3, 0 
  ble check_helmaroc_king_landing_timeout_return
  cmpwi r3, 3
  bge check_helmaroc_king_landing_timeout_return
  
  check_helmaroc_king_landing_timeout_check_timer:
  lha r3, 0xB0 (r30) ; Load our timer from the upper two bytes of HK's params.
  addi r3, r3, 1 ; Increment by one frame.
  sth r3, 0xB0 (r30) ; Store the new timer value.
  cmpwi r3, 10*30 ; 10 seconds is the limit for how long we allow HK to spend trying to land.
  ble check_helmaroc_king_landing_timeout_return
  
  check_helmaroc_king_landing_timeout_give_up:
  ; Went over the time limit. Force Helmaroc King to reset to flying instead of landing.
  li r0, 1
  sth r0, 0x2C6 (r30) ; Reset the state to 1, flying up. Corresponds to function up_fly(bdk_class *)
  li r0, 0
  sth r0, 0x2C8 (r30) ; Also reset the substate to 0 since we are leaving the landing state.
  
  check_helmaroc_king_landing_timeout_return:
  addi r11, r1, 0xA0 ; Replace the line we overwrote to jump here
  b 0x2AD4 ; Return to the end of the landing function
.close




; When Link opens a treasure chest, he teleports the enemy weapon he was carrying exactly to the
; position of his feet on the floor he's standing on. The enemy weapon then tries to search
; downwards for a floor. If Link is standing standing on only a single layer of floor above a void,
; this results in the weapon being unable to find the floor it's already on, because it's exactly at
; the position of that floor. As a failsafe, the weapon teleports itself to Link's feet again.
; However, after that failsafe is triggered, it also sets its Y position to 50 in absolute
; coordinates. This results in the weapon being vertically teleported to some arbitrary point in the
; room, or out of bounds. The devs likely intended to add 50 units to the foot pos so the weapon
; would visually fall a short distance instead of just teleporting, but they made a typo.
; In order to fix this, we remove the line that sets the Y pos to 50 and simply teleport it to
; Link's feet as normal instead.
.open "files/rels/d_a_boko.rel" ; Enemy weapon
.org 0x26A8 ; In daBoko_c::procCarry
  nop
.close
